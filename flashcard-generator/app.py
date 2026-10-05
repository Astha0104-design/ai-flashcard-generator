import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    print("HF_TOKEN not found!")
    exit()

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)

topic = input("Enter the topic for flashcards: ")

prompt = f"""
Create 5 simple flashcards about {topic}.

Format:

Flashcard 1
Question: ...
Answer: ...

Flashcard 2
Question: ...
Answer: ...

Flashcard 3
Question: ...
Answer: ...

Flashcard 4
Question: ...
Answer: ...

Flashcard 5
Question: ...
Answer: ...

Keep every answer short and easy to understand.
Put each flashcard on separate lines with a blank line between flashcards.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    max_tokens=500
)

print("\n========== AI FLASHCARDS ==========\n")
print(response.choices[0].message.content)