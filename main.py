from quart import Quart, request, jsonify, send_from_directory, send_file
from quart_cors import cors
import json

app = Quart(__name__)
app = cors(app, allow_origin="https://chat.openai.com")

@app.route('/.well-known/ai-plugin.json')
async def ai_plugin_json():
    return await send_from_directory('.well-known', 'ai-plugin.json')

@app.route('/openapi.yaml')
async def serve_openapi():
    return await send_file('openapi.yaml')

@app.route('/logo.png')
async def serve_logo():
    return await send_file('logo.png')

@app.route('/history', methods=['GET'])
async def history():
    # Get the search term from the query parameter (e.g., /history?search=hello)
    search_term = request.args.get('search', '')

    # Load the conversation history from the JSON file
    with open('conversations.json', 'r') as f:
        conversations = json.load(f)

    # Filter the conversation history based on the search term
    filtered_history = [entry for entry in conversations if search_term.lower() in entry.lower()]

    # Return the filtered conversation history as a response
    return jsonify({'history': filtered_history})


@app.route('/update_history', methods=['POST'])
async def update_history():
    data = await request.get_json()
    user_message = data.get('message', {}).get('content', '')
    assistant_message = data.get('assistant', {}).get('content', '')
    # Load the conversation history from the JSON file
    with open('conversations.json', 'r') as f:
        conversations = json.load(f)
    # Update the conversation history
    conversations[user_message] = assistant_message
    # Save the updated conversation history to the JSON file
    with open('conversations.json', 'w') as f:
        json.dump(conversations, f, indent=4)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5003)
