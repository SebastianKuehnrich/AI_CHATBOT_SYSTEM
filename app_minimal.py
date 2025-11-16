"""
Minimal Flask App für Railway Test
"""
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return jsonify({
        'status': 'online',
        'message': 'Minimal Test App läuft'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'ok',
        'message': 'Health endpoint funktioniert'
    })

@app.route('/api/test')
def test():
    return jsonify({
        'test': 'success',
        'message': 'Test endpoint funktioniert'
    })

@app.route('/api/personas')
def get_personas():
    personas = [
        {
            'key': '1',
            'name': 'Data Analyst Expert',
            'temperature': 0.3,
            'top_p': 0.8,
            'top_k': 40
        },
        {
            'key': '2',
            'name': 'Creative Storyteller',
            'temperature': 0.9,
            'top_p': 0.95,
            'top_k': 100
        },
        {
            'key': '3',
            'name': 'Technical Code Assistant',
            'temperature': 0.2,
            'top_p': 0.7,
            'top_k': 30
        },
        {
            'key': '4',
            'name': 'Business Consultant',
            'temperature': 0.4,
            'top_p': 0.85,
            'top_k': 50
        }
    ]
    return jsonify({'personas': personas})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

