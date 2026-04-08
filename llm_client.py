import requests
from config import API_URL, MODEL_NAME, TEMPERATURE, MAX_TOKENS
from prompts import SYSTEM_PROMPT


def get_llm_response(user_input):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS
    }

    response = requests.post(API_URL, json=payload, timeout=60)
    response.raise_for_status()

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {result}"