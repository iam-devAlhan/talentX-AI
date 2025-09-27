from fastapi import FastAPI, HTTPException
from db.config import connect_db
from routes.user_router import router as user_route
from bot import ask
from pydantic import BaseModel

app = FastAPI()
app.include_router(user_route)

connect_db()

class QueryBot(BaseModel):
    query: str


@app.get("/")
async def root():
    return {"message": "Server is running on 8000"}

@app.post("/ask")
async def ask_bot(request: QueryBot):
    response = ask(request.query)
    if not response:
        raise HTTPException(status_code=500, detail="Chatbot not responding!")
    return response