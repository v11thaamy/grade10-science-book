"""
Grade 10 Science Book — Backend Server
Holy Angel English School, Pokhara, Nepal
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import anthropic
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    try:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return jsonify({'error': 'API key not configured on server'}), 500

        data = request.get_json()
        prompt = data.get('prompt', '')
        system = data.get('system', 'You are an expert Grade 10 Science teacher for Nepal NEB/CDC SEE exam. Write comprehensive, detailed, textbook-quality content with Nepal context. Use markdown formatting.')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1500,
            system=system,
            messages=[{"role": "user", "content": prompt}]
        )

        return jsonify({'text': message.content[0].text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'app': 'Grade 10 Science Book'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
