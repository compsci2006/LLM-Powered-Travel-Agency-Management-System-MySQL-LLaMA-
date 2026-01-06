import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are an assistant that converts natural language into SQL queries.

Database schema:

Table: flight_agent
Columns:
- id
- firstname
- lastname
- age
- flight_airline
- flight_destination

Rules:
- Only generate SQL
- Allowed commands: SELECT, INSERT, UPDATE, DELETE
- Do NOT use DROP, TRUNCATE, ALTER
- Return ONLY SQL, no explanation
"""

def generate_sql(user_prompt):
    payload = {
        "model": "llama3",
        "prompt": f"{SYSTEM_PROMPT}\n\nUser request:\n{user_prompt}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    data = response.json()
    sql = data["response"].strip()

    return sql
