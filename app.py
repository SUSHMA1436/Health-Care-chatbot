from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_msg = data.get('message')

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful healthcare assistant."},
                {"role": "user", "content": user_msg}
            ],
            max_tokens=100,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({'reply': reply})

    except Exception as e:
        print("OpenAI Error:", e)  # ✅ This line helps debug
        return jsonify({'reply': "Sorry, there was an error processing your request."})


if __name__ == '__main__':
    app.run(debug=True)
