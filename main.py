import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "llama-3.1-8b-instant"

MODEL_CONFIG = {
    "technical": {
        "system_prompt": """You are a Technical Support Expert.
Be precise, structured, and code-focused.
Provide debugging steps and sample fixes when possible."""
    },
    "billing": {
        "system_prompt": """You are a Billing Support Specialist.
Be empathetic, polite, and policy-driven.
Clearly explain refund rules and billing policies."""
    },
    "general": {
        "system_prompt": """You are a friendly general assistant.
Answer casually and helpfully."""
    }
}

def get_bitcoin_price():
    return "The current Bitcoin price is $52,430 (mock value)."


def route_prompt(user_input):
    routing_prompt = f"""
Classify this text into one of these categories:
[technical, billing, general]

Return ONLY the category name.

Text:
{user_input}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,  # deterministic
        messages=[
            {"role": "system", "content": "You are a strict intent classifier."},
            {"role": "user", "content": routing_prompt}
        ]
    )

    category = response.choices[0].message.content.strip().lower().replace(".", "")
    return category



def process_request(user_input):

    if "bitcoin" in user_input.lower():
        return "tool", get_bitcoin_price()

    # Step 1: Route
    category = route_prompt(user_input)

    # Safety fallback
    if category not in MODEL_CONFIG:
        category = "general"

    # Step 2: Select Expert Prompt
    system_prompt = MODEL_CONFIG[category]["system_prompt"]

    # Step 3: Call Expert LLM
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,  # more flexible
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content

    return category, answer


if __name__ == "__main__":
    user_query = input("Enter your query: ")

    category, answer = process_request(user_query)

    print(f"CATEGORY: {category.upper()}")
    print("Response:\n")
    print(answer)