import os
import requests

DOC_URLS = [
    "https://raw.githubusercontent.com/sktime/sktime/main/examples/01_forecasting.ipynb",
    "https://raw.githubusercontent.com/sktime/sktime/main/examples/02_classification.ipynb",
    "https://raw.githubusercontent.com/sktime/sktime/main/README.md"
]

DATA_DIR = "data/raw"

def fetch_docs():
    os.makedirs(DATA_DIR, exist_ok=True)
    for url in DOC_URLS:
        filename = url.split("/")[-1]
        target_path = os.path.join(DATA_DIR, filename)
        print(f"Fetching {filename}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(target_path, "wb") as f:
                f.write(response.content)
            print(f"Saved to {target_path}")
        else:
            print(f"Failed to fetch {url}")

if __name__ == "__main__":
    fetch_docs()
