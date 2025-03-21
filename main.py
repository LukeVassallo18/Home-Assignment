from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio

# Initialise FastAPI app
app = FastAPI()

# Connecting to Mongo Atlas using provided connection string
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:123@mongodbcluster1.lnfxz.mongodb.net/")
db = client.multimedia_db # Accessing/Creating the multimedia database

# Definie a "constructor" for the player score data model
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

@app.get("/player_scores")
async def get_player_scores():
    scores = await db.scores.find({}, {"_id": 0}).to_list(length=None)
    return {"player_scores": str(scores)}
