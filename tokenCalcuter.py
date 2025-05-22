from flask import Flask, request, jsonify
import tiktoken

app = Flask(__name__)

@app.route("/count_tokens", methods=["POST"])
def count_tokens():
    data = request.get_json()
    text = data.get("text", "")
    model = data.get("model", "gpt-3.5-turbo")

    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        return jsonify({"error": f"Model '{model}' desteklenmiyor"}), 400

    tokens = encoding.encode(text)
    return jsonify({
        "token_count": len(tokens),
        "model": model
    })

@app.route("/", methods=["GET"])
def root():
    return "✅ GPT Token API çalışıyor. POST /count_tokens ile kullanabilirsiniz."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
