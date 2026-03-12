from fastapi import FastAPI
from enum import Enum

from src.pipeline.chat_engine import ask


app = FastAPI(title="Multi Source Intelligence Chatbot")


class RoleEnum(str, Enum):
    product = "product"
    tech = "tech"
    compliance = "compliance"


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/ask")
def query(
    question: str,
    role: RoleEnum = RoleEnum.product
):

    answer = ask(question, role.value)

    return {
        "question": question,
        "role": role,
        "answer": answer
    }