from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

@app.get("/health")
def health():
    return "service is online"
    

class PredictionRequest(BaseModel):
  query_string: str


@app.post("my-endpoint")
def my_endpoint(request: PredictionRequest):
  sentiment_model = pipeline("sentiment-analysis")

  sentiment_query_sentence = request.query_string
  sentiment = sentiment_model(sentiment_query_sentence)
  return sentiment
