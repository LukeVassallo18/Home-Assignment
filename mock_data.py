import asyncio
from database import db

async def insert_mock_data():
    # Insert sample sprite
    await db.sprites.insert_one({"filename": "sprite1.png", "content": b"fake_binary_data"})
    
    # Insert sample audio
    await db.audio.insert_one({"filename": "audio1.mp3", "content": b"fake_audio_binary"})
    
    # Insert sample player scores
    scores = [
        {"player_name": "Alice", "score": 100},
        {"player_name": "Bob", "score": 150},
        {"player_name": "Charlie", "score": 200}
    ]
    await db.scores.insert_many(scores)

    print("Mock data inserted successfully.")

# Run the async function
asyncio.run(insert_mock_data())
