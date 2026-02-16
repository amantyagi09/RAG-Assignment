# Simple RAG Project using Google Gemini
This repository contains a small Retrieval-Augmented Generation (RAG) application built using Google Gemini. 
It is designed to evaluate understanding of end-to-end RAG architecture. 
The application ingests local text documents, indexes them using a vector database, and retrieves the most relevant document chunks to pass to Google Gemini to generate an answer.

## 🛠️ Tech Stack
* **Backend:** Python with FastAPI 
* **Frontend:** Streamlit (implementing the optional simple UI bonus) 
* **LLM & Embeddings:** Google Gemini API (`gemini-2.5-flash` and `gemini-embedding-001`) 
* **Vector Database:** ChromaDB

## 📋 Prerequisites
1. Python 3.11.9 installed.
2. A Google Gemini API Key.

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amantyagi09/RAG-Assignment.git
   cd <your-project-folder>
   
2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   
3. **Environment Setup:**
   Create a .env file in the root directory and add your API key.
   
5. **Data Preparation:**
   
   
