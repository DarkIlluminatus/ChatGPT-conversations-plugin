from pymongo import MongoClient
from quart import Quart, request, jsonify, send_from_directory, send_file
from quart_cors import cors
import json
import os
from pymongo import MongoClient

app = Quart(__name__)
app = cors(app, allow_origin="https://chat.openai.com")

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['chatgpt_database']  # Use your database name here
conversations_collection = db['conversations']  # Use your collection name here
model_comparisons_collection = db['model_comparisons']  # Use your collection name here

@app.route('/.well-known/ai-plugin.json')
async def ai_plugin_json():
    return await send_from_directory(os.path.join(os.getcwd(), '.well-known'), 'ai-plugin.json')

@app.before_serving
async def create_databases():
    # Create the databases and collections if they don't exist
    db_list = client.list_database_names()
    if 'chatgpt_database' not in db_list:
        db = client['chatgpt_database']
        db.create_collection('conversations')
        db.create_collection('model_comparisons')

@app.route('/openapi.yaml')
async def serve_openapi():
    return await send_file('openapi.yaml')

@app.route('/logo.png')
async def serve_logo():
    return await send_file('logo.png')

@app.route('/model_comparisons', methods=['GET'])
async def get_model_comparisons():
    # Retrieve all model comparisons from the collection
    model_comparisons = list(model_comparisons_collection.find())
    return jsonify(model_comparisons)

@app.route('/conversations/<conversation_id>', methods=['GET'])
async def get_conversation(conversation_id):
    # Retrieve a specific conversation by its ID from the collection
    conversation = conversations_collection.find_one({'id': conversation_id})
    if conversation:
        return jsonify(conversation)
    else:
        return jsonify({'error': 'Conversation not found'}), 404

@app.route('/conversations/search', methods=['GET'])
async def search_conversations():
    query = request.args.get('query', '')
    # Search for conversations containing the specified query term
    conversations = list(conversations_collection.find({'$text': {'$search': query}}))
    return jsonify(conversations)

@app.route('/conversations', methods=['POST'])
async def add_conversation():
    conversation = await request.get_json()
    # Insert the new conversation into the collection
    result = conversations_collection.insert_one(conversation)
    return jsonify({'status': 'success', 'conversation_id': str(result.inserted_id)})

@app.route('/conversations/<conversation_id>', methods=['PUT'])
async def update_conversation(conversation_id):
    conversation = await request.get_json()
    # Update the existing conversation with the specified ID
    result = conversations_collection.update_one({'id': conversation_id}, {'$set': conversation})
    if result.modified_count > 0:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Conversation not found'}), 404

@app.route('/analyze', methods=['POST'])
async def analyze_conversation():
    data = await request.get_json()
    conversation_id = data.get('conversation_id', '')
    # Retrieve the conversation from the collection
    conversation = conversations_collection.find_one({'id': conversation_id})
    if conversation:
        # Perform analysis on the conversation
        # Your analysis code goes here
        # ...
        return jsonify({'status': 'success'})
    else:
        return jsonify({'error': 'Conversation not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)
