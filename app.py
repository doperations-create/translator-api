from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

# ✅ Home route (for testing in browser)
@app.route('/')
def home():
    return "Translator API is running 🚀"

# ✅ Translation route (supports BOTH GET and POST)
@app.route('/translate', methods=['GET', 'POST'])
def translate_text():

    # 👉 If request is from browser (GET)
    if request.method == 'GET':
        text = request.args.get("text", "")
        target = request.args.get("target", "en")

    # 👉 If request is from app/Postman (POST)
    else:
        data = request.get_json()
        text = data.get("text", "")
        target = data.get("target", "en")

    # ❌ If no text
    if not text:
        return jsonify({"error": "Text is required"}), 400

    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)