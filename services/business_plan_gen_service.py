from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_full_business_plan(session, history):
    from utils.progress import TOTALS_BY_PHASE

    messages = [
        {
            "role": "system",
            "content": "You are a business planning assistant. Generate a full business plan using the user's prior answers."
        },
        {
            "role": "user",
            "content": f"Based on this user profile and prior responses, create a business plan.\n\nSession Info:\n{session}\n\nChat History:\n{history}"
        }
    ]

    response = await client.chat.completions.create(
        model="gpt-4o-search-preview",
        messages=messages,
    )

    return {
        "plan": response.choices[0].message.content
    }
