import os
import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatgpt_database']  # Use your database name here
collection = db['conversations']  # Use your collection name here

# Define the path to the data files
data_path = 'filesforimport'

# Check if the data files exist
if not os.path.exists(data_path):
    print("Error: No data found for import. Please export your data and place it in the necessary folders.")
    input("Press Enter to exit...")
    exit(1)

# Load and import each JSON data file
for filename in os.listdir(data_path):
    if filename == 'conversations.json':
        with open(os.path.join(data_path, filename)) as f:
            data = json.load(f)
            # Transform the data to match the ConversationSchema
            transformed_data = [{
                'id': conv['id'],
                'timestamp': conv['timestamp'],
                'participants': conv['participants'],
                'messages': conv['messages']
            } for conv in data]
            collection.insert_many(transformed_data)
