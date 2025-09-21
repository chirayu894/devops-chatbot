from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=['POST'])
def ask():
    response = {"answer": "This is a response from my DevOps-deployed chatbot!"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
