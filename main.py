# app/main.py

from fastapi import FastAPI
from app.api import chat as chat_api
app = FastAPI()

app.include_router(chat_api.router)

@app.get("/ping")
def ping():
     return {"status": "ok"}

