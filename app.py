from src.main_evaluator import Evaluator
from flask import Flask, request, jsonify, Response
from waitress import serve
import json
app = Flask(__name__)

@app.route('/', methods=["GET"])
def info_view():
    """List of routes for this API."""
    output = {
        'evaluate': 'GET /evaluate/<userID>/<income>/<childBirthYear>'
    }
    return jsonify(output)

@app.route('/evaluate/<userID>/<income>/<childBirthYear>', methods=['GET'])
def evaluate(userID, income, childBirthYear):
    try:
        evaluator = Evaluator(userID, income, childBirthYear)
        response = evaluator.evaluate()
        status_code = 200
    except KeyError or TypeError:
        response = "Faulty JSON. Please provide proper JSON in request body"
        status_code = 400

    return Response(response, status_code)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)