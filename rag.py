import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")

# Chroma
client = chromadb.PersistentClient(path=CHROMA_DIR)

# Gemini client
api_key = os.getenv("GEMINI_API_KEY")
client_gemini = genai.Client(api_key=api_key)

LLM_MODEL = "models/gemini-2.5-flash"      
EMBED_MODEL = "models/gemini-embedding-001"


def get_embedding(text: str):
    emb = client_gemini.models.embed_content(
        model=EMBED_MODEL,
        contents=text
    )
    return emb.embeddings[0].values


def ask_rag(query: str, top_k: int = 3):
    try:
        collection = client.get_or_create_collection(name="rag_docs")

        query_embedding = get_embedding(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        if not results["documents"] or not results["documents"][0]:
            return {
                "answer": "No relevant documents found.",
                "sources": []
            }

        docs = results["documents"][0]
        sources = [m.get("source", "unknown") for m in results["metadatas"][0]]

        context = "\n\n".join(docs)

        prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

        response = client_gemini.models.generate_content(
            model=LLM_MODEL,
            contents=prompt
        )

        return {
            "answer": response.text,
            "sources": sources
        }

    except Exception as e:
        return {
            "answer": f"RAG error: {str(e)}",
            "sources": []
        }
