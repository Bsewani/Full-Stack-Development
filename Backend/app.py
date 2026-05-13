from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_mentor(request: ChatRequest):
    try:
        # Talking to Ollama
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': 'You are a pro L&D mentor.'},
            {'role': 'user', 'content': request.question}
        ])
        return {"answer": response['message']['content']}
    except Exception as e:
        return {"answer": f"Error: {str(e)}"}

# Do NOT add app.run() here. Let Uvicorn handle it.