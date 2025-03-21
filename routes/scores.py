from fastapi import APIRouter
from database import db
from models import PlayerScore

# Initialize router
router = APIRouter()

@router.post("/player_score")
async def add_score(score: PlayerScore):
    """
    Records a player's score in the database.
    """
    score_doc = score.dict()
    result = await db.scores.insert_one(score_doc)
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@router.get("/player_scores")
async def get_player_scores():
    """
    Retrieves all player scores from the database.
    """
    scores = await db.scores.find({}, {"_id": 0}).to_list(length=None)
    return {"player_scores": str(scores)}