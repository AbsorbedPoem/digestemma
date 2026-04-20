from fastapi import FastAPI
from lib.inference import Inference

app:FastAPI = FastAPI(debug=True)

@app.post('/chat/')
async def home(prompt: str):
    return await Inference(prompt)
