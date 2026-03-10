from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

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
    # AI Analysis
    blob = TextBlob(input.data)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.2:
        signal = "STRONG POSITIVE SIGNAL"
        action = "BUY"
    elif sentiment < -0.2:
        signal = "STRONG NEGATIVE SIGNAL"
        action = "SELL"
    else:
        signal = "NEUTRAL SIGNAL"
        action = "HOLD"

    return {
        "received": input.data,
        "signal": signal,
        "action": action,
        "confidence": round(abs(sentiment) * 100, 2),
        "status": "AI analysis complete"
    }