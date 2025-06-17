from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from your AI Flask server!'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # For now, just echo back with a pretend AI reply
    bot_reply = f"You said: {user_message}. I say: 'This is a dummy AI response.'"

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
