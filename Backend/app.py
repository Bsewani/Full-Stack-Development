from flask import Flask, request, jsonify
from flask_cors import CORS  # You may need to run: pip install flask-cors
import ollama

# 1. Initialize the Flask application
app = Flask(__name__)
CORS(app)  # This allows your Streamlit app to communicate with Flask without being blocked

@app.route('/ask', methods=['POST'])
def process_question():
    # 2. Read the incoming request
    data = request.get_json()
    user_question = data.get("question", "")
    
    if not user_question:
        return jsonify({"answer": "I didn't receive a question. Please try again!"}), 400

    print(f"L&D Mentor received: {user_question}")

    try:
        # 3. The AI Logic: Connecting to Ollama
        # We add a 'system' prompt to keep the AI in its "L&D Mentor" persona
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'system',
                'content': 'You are a professional Learning and Development (L&D) mentor. '
                           'Provide concise, encouraging, and actionable career advice.'
            },
            {
                'role': 'user',
                'content': user_question,
            },
        ])

        # 4. Extract the LLM's text response
        ai_answer = response['message']['content']

    except Exception as e:
        print(f"Error: {e}")
        ai_answer = "I'm having trouble reaching my brain (Ollama). Is it running?"

    # 5. Send the real answer back
    return jsonify({"answer": ai_answer})

if __name__ == '__main__':
    # Runs locally on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)