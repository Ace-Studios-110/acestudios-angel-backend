from openai import AsyncOpenAI
import os
from utils.constant import ANGEL_SYSTEM_PROMPT

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TAG_PROMPT = "Reminder: Before asking the next question, include a machine-readable tag in this format:\n[[Q:<PHASE>.<NN>]] — e.g. [[Q:BUSINESS_PLAN.03]] What is your pricing model?"

INTRO_INSTRUCTION = """
Please introduce yourself as Angel, the user's proactive entrepreneurship-support AI assistant on the Founder platform. Then immediately begin the onboarding flow by asking:
[[Q:KYC.01]] What is your full legal name?
"""

async def get_angel_reply(user_msg, history):
    is_empty = not user_msg.get("content") or user_msg["content"].strip() == ""
    is_first = len(history) == 0 and is_empty

    msgs = [
        {"role": "system", "content": ANGEL_SYSTEM_PROMPT},
        {"role": "system", "content": TAG_PROMPT},
    ]

    if is_first:
        msgs.append({"role": "user", "content": "hi"})
        msgs.append({"role": "user", "content": INTRO_INSTRUCTION})
    else:
        msgs.extend(history)
        msgs.append({"role": "user", "content": user_msg["content"].strip()})

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=msgs,
        temperature=0.7   
    )

    return response.choices[0].message.content
