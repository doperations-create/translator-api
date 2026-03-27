from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# ✅ ADD THIS
@app.route('/')
def home():
    return "Translator API is running 🚀"

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    text = data.get("text", "")
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)