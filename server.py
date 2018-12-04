from flask import Flask, jsonify, request, make_response

import os

app = Flask(__name__)
addr = os.environ["ADDR"]
port = addr.split(":")[1]
host = addr.split(":")[0]

@app.route("/v1/beer", methods=["POST"])
def beer_handler():
    model_features = request.get_json()
    if model_features is None:
        return make_response("Request Body Cannot Be Empty", 404)
    return jsonify({"jsondata": model_features})

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)

