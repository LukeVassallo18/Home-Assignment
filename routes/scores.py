from fastapi import APIRouter, File, UploadFile, HTTPException
from database import db

# Initialize router
router = APIRouter()

@router.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    """
    Uploads a sprite file to the database.
    """
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}