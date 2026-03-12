# Multi-Source Intelligence Chatbot System

AI Engineer Assignment – Production Grade Intelligent Chatbot

This project implements a multi-source intelligence chatbot that scrapes regulatory and financial data, processes documents, builds a semantic vector database, and provides role-based responses for different stakeholders.

The system integrates NPCI circulars and RBI ATM statistics and allows Product, Tech, and Compliance roles to query the knowledge base.

---

## 🚀 Features

- NPCI circular scraper
- RBI ATM statistics scraper
- OCR fallback for scanned PDFs
- Document processing pipeline
- Semantic chunking
- Embeddings using BGE model
- FAISS vector database
- Multi-source retrieval
- Role-based chatbot responses
- FastAPI API service
- Swagger UI interface
- Groq LLM integration

---

## 🧠 System Architecture
NPCI + RBI Websites
    ↓
Web Scrapers
    ↓
Document Processing
(PDF + OCR + Tables)
    ↓
Chunking
    ↓
Embeddings (BGE)
    ↓
FAISS Vector DB
    ↓
Query Engine
    ↓
Role-based Prompt
    ↓
Groq LLM
    ↓
Chatbot / API

---

## 📂 Project Structure

src/
api/
ingestion/
pipeline/
scraper/
utils/

data/
vector_store/
logs/
README.md
requirements.txt

---

## ⚙️ Installation

### 1. Clone repository
git clone https://github.com/yourusername/intelligence-chatbot.git

cd intelligence-chatbot


### 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate


### 3. Install dependencies
pip install -r requirements.txt

## 🔑 Environment Variables

Create `.env`

GROQ_API_KEY=your_api_key_here

Do not commit this file.

---

## 📥 Run Scrapers

python -m src.scraper.npci_scraper
python -m src.scraper.rbi_scraper

Downloads circulars and ATM data.

---

## 📦 Build Vector Database

python -m src.pipeline.ingest_pipeline

Creates:

vector_store/faiss.index
vector_store/docs.pkl

---

## 💬 Run Chat (CLI)

python -m src.pipeline.chat

Select role:

product
tech
compliance

---

## 🌐 Run API Server


uvicorn src.api.app:app --reload

Open:

http://127.0.0.1:8000/docs

Swagger UI allows selecting role from dropdown.

---

## 👥 Supported Roles

| Role | Description |
|------|------------|
| product | Product insights |
| tech | Technical analysis |
| compliance | Regulatory interpretation |

---

## 📊 Data Sources

- https://www.npci.org.in/circulars/upi
- https://rbi.org.in/scripts/ATMView.aspx

---

## ⚠ Notes

- Vector store not committed to Git
- API key not stored in repo
- Supports scanned PDFs using OCR
- Works within 8GB RAM constraint

---

## 👨‍💻 Author

Abhinav Dubey

AI Engineer Assignment – Multi Source Intelligence Chatbot