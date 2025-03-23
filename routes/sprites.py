from fastapi import APIRouter, File, UploadFile, HTTPException
from database import db

# Initialize router
router = APIRouter()

# Handles the upload of a sprite file to the database.

# Endpoint:
#     POST /upload_sprite

# Parameters:
#     file (UploadFile): The sprite file to be uploaded. This is expected to be 
#     provided as a file upload in the request.

# Returns:
#     dict: A dictionary containing a success message and the ID of the inserted 
#     sprite document in the database.

# Raises:
#     HTTPException: If there is an issue with the file upload or database insertion.

@router.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    """
    Uploads a sprite file to the database.
    """
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}