"""Simple Flask API that requires several secrets to function."""

import os

from flask import Flask, jsonify

app = Flask(__name__)

# Required secrets
DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]
JWT_SECRET = os.environ["JWT_SECRET"]

# Optional config
PORT = int(os.environ.get("PORT", "5000"))
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/")
def index():
    return jsonify({"message": "R Tutorials API"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
