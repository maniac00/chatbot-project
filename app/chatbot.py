import os
from openai import AsyncOpenAI  # AsyncOpenAI로 변경
from dotenv import load_dotenv

load_dotenv()

class ChatBot:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    async def get_response(self, message):
        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",  # 올바른 모델명으로 수정
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content