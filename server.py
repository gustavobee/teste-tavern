from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/dobra", methods=["POST"])
def dobra_numero():
    r = request.get_json()

    try:
        numero = r["numero"]
    except (KeyError, TypeError):
        return jsonify({"error": "nenhum número foi passado"}), 400

    try:
        dobro = int(numero)*2
    except ValueError:
        return jsonify({"error": "um número não foi passado"}), 400

    return jsonify({"dobro": dobro}), 200