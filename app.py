
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "IMAGIA - Serveur opérationnel"

@app.route("/create", methods=["POST"])
def create_video():
    data = request.get_json(silent=True) or {}

    idea = data.get("idea", "").strip()
    duration = data.get("duration", "30")
    video_format = data.get("format", "9:16")

    if not idea:
        return jsonify({"error": "Décris ton idée de vidéo."}), 400

    return jsonify({
        "success": True,
        "message": "Ton idée a été reçue par le serveur IMAGIA.",
        "idea": idea,
        "duration": duration,
        "format": video_format
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
