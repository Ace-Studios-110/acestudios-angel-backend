from db.supabase import supabase

async def fetch_chat_history(session_id: str):
    response = supabase.from_("chat_history").select("role, content").eq("session_id", session_id).order("created_at").execute()
    return response.data

async def save_chat_message(session_id: str, user_id: str, role: str, content: str):
    supabase.from_("chat_history").insert({"session_id": session_id, "user_id": user_id, "role": role, "content": content}).execute()

