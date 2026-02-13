from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.get("/todos")
def get_todos():
    return []
