import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")   # put your docs here
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")

# Gemini client
client_gemini = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EMBED_MODEL = "models/gemini-embedding-001"

# Chroma
client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(name="rag_docs")


def get_embedding(text: str):
    emb = client_gemini.models.embed_content(
        model=EMBED_MODEL,
        contents=text
    )
    return emb.embeddings[0].values


def load_files():
    docs = []
    metadatas = []
    ids = []

    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        if not os.path.isfile(path):
            continue

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        docs.append(text)
        metadatas.append({"source": filename})
        ids.append(filename)

    return docs, metadatas, ids


docs, metadatas, ids = load_files()

print(f"Ingesting {len(docs)} documents...")

for i, doc in enumerate(docs):
    embedding = get_embedding(doc)

    collection.add(
        documents=[doc],
        metadatas=[metadatas[i]],
        ids=[ids[i]],
        embeddings=[embedding]
    )

print("✅ Ingestion complete")
