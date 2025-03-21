# Setup Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Prequisites](#prerequisites)
3. [Setup](#setup)
4. [Installation](#installation)
5. [Github Connection Setup](#github-connection-setup)
6. [Vercel](#create-verceljson-file)
## Explanation
This is the setup documentation for a restful API which connects to a MongoDB databse and hosts all the endpoints on a localhost server or on Vercel with github syncronizations

## Prerequisites
- Make sure python 3.9+ is installed on the system

## Setup:
1. Create main.py file and input follwing code
```python
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio

app = FastAPI()

# Connect to Mongo Atlas
client = motor.motor_asyncio.AsyncIOMotorClient("your_mongo_connection_string")
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    # In a real application, the file should be saved to a storage service
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}

@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}
```

## Installation
1. Install dependencies:
    ```bash
    pip install fastAPI

    pip install uvicorn

    pip install motor

    pip install pydantic

    pip install python-dotenv

    pip install requests

    # Optionally
    pip install python-multipart
    ```

## Freeze dependencies into a text file:
```bash
pip freeze > requirements.txt
```
## Create virtual python environment:
```bash
python -m venv env
```

## Run python file
```bash
    uvicorn main:app --reload
```

## Github Connection Setup
1. Publish to new github repo

2. Deploy to get URL

3. Connect vercel to github and import local repo

## Create vercel.json file
Input following code:
```json
{
    "version": 2,
    "builds": [
      {
        "src": "main.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "main.py"
      }
    ]
  }
```

## Navigate to Vercel
##### Click Vercel link that is provided immediately and add /docs to the end of the url to use the endpoints

## Luke Vassallo 6.2A Setup Documentation