from flask import Flask, render_template, request, jsonify
from banker import is_safe_state, request_resources

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/api/banker")
def banker_check():
    data = request.get_json(silent=True) or {}
    try:
        result = is_safe_state(data["available"], data["allocation"], data["maximum"])
        return jsonify(result)
    except (KeyError, TypeError, ValueError) as exc:
        return jsonify({"error": str(exc)}), 400

@app.post("/api/banker/request")
def banker_request():
    data = request.get_json(silent=True) or {}
    try:
        result = request_resources(
            data["available"], data["allocation"], data["maximum"],
            int(data["process"]), data["request"]
        )
        return jsonify(result)
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        return jsonify({"error": str(exc)}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
