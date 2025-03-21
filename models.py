from pydantic import BaseModel

# Pydantic model for player scores
class PlayerScore(BaseModel):
    player_name: str
    score: int