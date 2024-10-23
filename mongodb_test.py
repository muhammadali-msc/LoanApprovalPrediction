from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import os

# Load environment variables from .env file
load_dotenv()

# Accessing the environment variables
mongo_db_username = os.getenv('mongo_db_username')
mongo_db_password = os.getenv('mongo_db_password')



uri = "mongodb+srv://"+ mongo_db_username+ ":" + mongo_db_password + "@loanapprovalmongobd.rridu.mongodb.net/?retryWrites=true&w=majority&appName=LoanApprovalMongoBD"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)