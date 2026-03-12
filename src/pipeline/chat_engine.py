import os
from dotenv import load_dotenv
from groq import Groq
from src.pipeline.query_engine import QueryEngine

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

engine = QueryEngine()

ROLE_PROMPTS = {
    "product": "You are a Product Lead analyzing market and product implications.",
    "tech": "You are a Tech Lead analyzing system architecture, APIs and infrastructure.",
    "compliance": "You are a Compliance Lead interpreting regulatory implications.",
}

def ask(query, role="product"):

    context = engine.search(query, k=5)
    context_text = "\n\n".join(context)

    role_prompt = ROLE_PROMPTS.get(role, ROLE_PROMPTS["product"])

    prompt = f"""
{role_prompt}

You analyze RBI and NPCI documents.

Context:
{context_text}

Question:
{query}

Provide a clear answer tailored for the {role} role.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content