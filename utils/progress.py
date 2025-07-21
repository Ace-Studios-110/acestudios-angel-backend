from typing import Optional

def parse_tag(text: str) -> Optional[str]:
    import re
    match = re.search(r"\[\[Q:([A-Z_]+\.\d{2})]]", text)
    return match.group(1) if match else None

def is_answer_valid(q_tag: str, answer: str) -> bool:
    return answer.strip() and len(answer.strip()) > 3

TOTALS_BY_PHASE = {
    "KYC": 20,
    "BUSINESS_PLAN": 9,
    "ROADMAP": 0,
    "IMPLEMENTATION": 0
}
