from fastapi import APIRouter, File, UploadFile, HTTPException
from database import db

# Initialize router
router = APIRouter()

# Handles the upload of an audio file to the database.

# Endpoint:
#     POST /upload_audio

# Parameters:
#     file (UploadFile): The audio file to be uploaded. This is a required parameter.

# Returns:
#     dict: A dictionary containing a success message and the ID of the inserted audio document in the database.

# Raises:
#     HTTPException: If there is an issue with file reading or database insertion.

@router.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    """
    Uploads an audio file to the database.
    """
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}