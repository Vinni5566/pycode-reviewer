import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from .ingestion import SktimeDocLoader

class SktimeRetriever:
    def __init__(self, model_name="all-MiniLM-L6-v2", index_path="data/faiss_index"):
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)
        self.index_path = index_path
        self.vector_store = None

    def build_index(self, data_dir: str):
        """Load documents and build a new FAISS index."""
        loader = SktimeDocLoader()
        chunks = loader.process_directory(data_dir)
        
        if not chunks:
            print("No documents found to index.")
            return
        
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        self.vector_store.save_local(self.index_path)
        print(f"Index built and saved to {self.index_path}")

    def load_index(self):
        """Load an existing FAISS index."""
        if os.path.exists(self.index_path):
            self.vector_store = FAISS.load_local(
                self.index_path, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
            return True
        return False

    def search(self, query: str, k: int = 3):
        """Search for relevant snippets."""
        if not self.vector_store:
            if not self.load_index():
                raise ValueError("Index not found. Please build the index first.")
        
        docs = self.vector_store.similarity_search(query, k=k)
        return docs

if __name__ == "__main__":
    retriever = SktimeRetriever()
    print("Retriever initialized.")
