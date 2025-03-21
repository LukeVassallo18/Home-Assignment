import motor.motor_asyncio

# MongoDB connection string
MONGO_URI = "mongodb+srv://admin:123@mongodbcluster1.lnfxz.mongodb.net/"

# Initialize MongoDB client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# Access the multimedia database
db = client.multimedia_db