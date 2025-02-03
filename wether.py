from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suggest-clothing', methods=['POST'])
def suggest_clothing():
    data = request.json
    temperature = data.get('temperature')

    if temperature is None:
        return jsonify({"error": "No temperature provided"}), 400

    try:
        temperature = float(temperature)
    except ValueError:
        return jsonify({"error": "Invalid temperature value"}), 400

    if temperature < 15:
        suggestion = "Use roupas quentes, como casacos, cachecóis e luvas."
    elif 15 <= temperature <= 25:
        suggestion = "Use roupas confortáveis de meia estação, como calças e camisetas de manga comprida."
    else:
        suggestion = "Use roupas leves, como shorts e camisetas."

    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
