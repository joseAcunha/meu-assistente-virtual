from fastapi import FastAPI
from pydantic import BaseModel
from src.assistente import chat_with_assistant
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Assistente Virtual de E-commerce",
    description="API para o assistente virtual inteligente.",
    version="1.0.0"
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "file://",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    user_message = request.message
    assistant_response = chat_with_assistant(user_message)
    return ChatResponse(response=assistant_response)

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Assistente Virtual de E-commerce! Acesse /docs para a documentação da API."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)