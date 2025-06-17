from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from your AI Flask server!'

@app.route('/chat-ui')
def chat_ui():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple AI Chat</title>
            <style>
                body { font-family: sans-serif; padding: 2em; }
                input, button { padding: 0.5em; font-size: 1em; }
                #response { margin-top: 1em; color: green; }
            </style>
        </head>
        <body>
            <h2>Fake AI Chat</h2>
            <input type="text" id="message" placeholder="Say something..." />
            <button onclick="sendMessage()">Send</button>
            <div id="response"></div>

            <script>
                async function sendMessage() {
                    const msg = document.getElementById('message').value;
                    const res = await fetch('/chat', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message: msg })
                    });
                    const data = await res.json();
                    document.getElementById('response').textContent = data.response;
                }
            </script>
        </body>
        </html>
    ''')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    # For now, just echo back with a pretend AI reply
    bot_reply = f"You said: {user_message}. I say: 'This is a dummy AI response.'"

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
