from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "AI Service Running"})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
