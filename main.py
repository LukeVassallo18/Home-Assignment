from fastapi import FastAPI
from routes import sprites, audio, scores

# Initialize FastAPI app
app = FastAPI()

# Include routes from different modules
app.include_router(sprites.router)
app.include_router(audio.router)
app.include_router(scores.router)