from fastapi import FastAPI

app = FastAPI(title="Hello World API")


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}