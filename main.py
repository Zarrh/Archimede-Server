from flask import Flask, send_file, send_from_directory
import os

app = Flask(__name__)
PORT = 5555

frontend_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../front-end/dist')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(frontend_folder, filename)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_index(path):
    return send_file(os.path.join(frontend_folder, 'index.html'))

if __name__ == "__main__":
    app.run(port=PORT)