from fastapi import FastAPI
from rag import ask_rag

app = FastAPI()

@app.get("/ask")
def ask(query: str, top_k: int = 3):
    result = ask_rag(query, top_k)
    return result