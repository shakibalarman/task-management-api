
from fastapi import FastAPI

app = FastAPI(
    title="Task Management API",
    description="A REST API for managing tasks.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
