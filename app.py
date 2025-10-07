
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running successfully!"})

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    ingredients = data.get("ingredients", [])
    
    # Just a simple example — returns the ingredients received
    return jsonify({
        "received_ingredients": ingredients,
        "message": "Feature for recipe suggestions will be added soon."
    })

if __name__ == "__main__":
    app.run(debug=True)

