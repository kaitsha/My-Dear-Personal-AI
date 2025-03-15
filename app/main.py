from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from utils.chat import chat_with_ai
from utils.tts import text_to_speech

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, my dear! I am ready to assist you."}

@app.post("/chat/")
def chat(message: str):
    reply = chat_with_ai(message)
    return {"reply": reply}

@app.post("/add_task/")
def add_task(task: str):
    with open("app/tasks.json", "r+") as file:
        tasks = json.load(file)
        tasks.append(task)
        file.seek(0)
        json.dump(tasks, file, indent=4)
    return {"message": "Task added successfully!"}

@app.get("/get_tasks/")
def get_tasks():
    with open("app/tasks.json", "r") as file:
        tasks = json.load(file)
    return {"tasks": tasks}
