import os
import nbformat
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

class SktimeDocLoader:
    def __init__(self, chunk_size=1000, chunk_overlap=100):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )

    def load_notebook(self, file_path: str):
        """Extract text and code from a Jupyter notebook."""
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        content = []
        for cell in nb.cells:
            if cell.cell_type == 'markdown':
                content.append(cell.source)
            elif cell.cell_type == 'code':
                content.append(f"```python\n{cell.source}\n```")
        
        full_text = "\n\n".join(content)
        metadata = {"source": file_path, "type": "notebook"}
        return [Document(page_content=full_text, metadata=metadata)]

    def load_markdown(self, file_path: str):
        """Load text from a markdown file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        metadata = {"source": file_path, "type": "markdown"}
        return [Document(page_content=content, metadata=metadata)]

    def process_directory(self, directory_path: str):
        """Process all supported files in a directory."""
        documents = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.ipynb'):
                    documents.extend(self.load_notebook(file_path))
                elif file.endswith('.md'):
                    documents.extend(self.load_markdown(file_path))
        
        chunks = self.text_splitter.split_documents(documents)
        return chunks

if __name__ == "__main__":
    # Example usage
    loader = SktimeDocLoader()
    print("Loader initialized. Use process_directory() to chunk documentation.")
