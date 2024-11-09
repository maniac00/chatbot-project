from fastapi import FastAPI
from pydantic import BaseModel
from .chatbot import ChatBot

app = FastAPI()
chatbot = ChatBot()

class Message(BaseModel):
    content: str

@app.post("/chat")
async def chat(message: Message):
    response = await chatbot.get_response(message.content)
    return {"response": response}