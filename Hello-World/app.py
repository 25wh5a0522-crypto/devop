from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello World from Python on Azure App Service saurav.bansode + Bhumika + Danush", 200

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
