from fastapi import FastAPI
from db.config import connect_db
from routes.user_router import router as user_route

app = FastAPI()
app.include_router(user_route)
connect_db()

@app.get("/")
async def root():
    return {"message": "Server is running on 8000"}

