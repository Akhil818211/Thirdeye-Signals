from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This defines what data the AI expects to receive
class SignalInput(BaseModel):
    data: str

@app.get("/")
def home():
    return {"message": "Thirdeye Signals API is live!"}

@app.get("/status")
def status():
    return {"status": "running", "company": "Thirdeye Signals"}

@app.post("/predict")
def predict(input: SignalInput):
    # AI model will go here later
    return {
        "received": input.data,
        "prediction": "AI model not connected yet",
        "status": "ready for AI"
    }