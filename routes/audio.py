from fastapi import APIRouter, File, UploadFile, HTTPException
from database import db

# Initialize router
router = APIRouter()

@router.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    """
    Uploads an audio file to the database.
    """
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}