from flask import Flask, render_template, request, jsonify
from BotDefinition import OpenAIBot

app = Flask(__name__)
chatbot = OpenAIBot("anthropic/claude-2")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Please provide a message'}), 400

        user_message = data['message'].strip()
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400

        print(f"Processing message: {user_message}")
        response = chatbot.generate_response(user_message)
        
        if response:
            print(f"Bot response: {response}")
            return jsonify({'response': response})
        else:
            print("No response received from bot")
            return jsonify({'error': 'No response from the chatbot'}), 500

    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    print("Starting ChatBot server...")
    app.run(debug=True, port=5000) 