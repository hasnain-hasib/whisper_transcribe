from fastapi import FastAPI, File, UploadFile, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import time
import psutil
import whisper
import tempfile
import openai

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with open("index.html", "r") as f:
        content = f.read()
    return HTMLResponse(content=content)
@app.post("/transcribe")
async def transcribe_audio(
    audio_file: UploadFile = File(...),
    api_key: str = Query("", description="APIkey"),
):
    openai.api_key = api_key
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(await audio_file.read())
        temp_file_path = temp_file.name

    model = whisper.load_model("base")
    result = model.transcribe(temp_file_path)
    transcription = result["text"]
    print(transcription)  

    os.unlink(temp_file_path) 

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=transcription,
    max_tokens=3000,
    n=1,
    frequency_penalty=1,
    presence_penalty=1,
    stop=None,
    temperature=0.8,
    top_p=1,best_of=1 )
    

    response = {
        "Audio_Transcript": transcription,
        "Answer": response,
    }

    return response
