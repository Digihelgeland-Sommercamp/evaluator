from src.main_evaluator import Evaluator
from flask import Flask, request, jsonify, Response
from waitress import serve
import json
app = Flask(__name__)

@app.route('/', methods=["GET"])
def info_view():
    """List of routes for this API."""
    output = {
        'info': 'GET /',
        'evaluate': 'GET /evaluate'
    }
    return jsonify(output)

@app.route('/evaluate', methods=['GET'])
def evaluate():
    request_data = request.get_json()
    print(request_data)

    if not isinstance(request_data, dict):
        request_data = json.loads(request_data)

    if request_data != None:
        try:
            evaluator = Evaluator(request_data)
            response = evaluator.evaluate()
            status_code = 200
        except KeyError or TypeError:
            response = "Faulty JSON. Please provide proper JSON in request body"
            status_code = 400
    else: 
        response = "No JSON data in body. Please provide proper JSON in request body"
        status_code = 400
    return Response(response, status_code)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)