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

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

