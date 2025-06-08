from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def home():
    return "Hello , FASTAPI server is running"