
# Python Imports
import time
from http import HTTPStatus

# Third Party Imports
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def ping():
    return (jsonify({"timestamp": int(time.time())}), HTTPStatus.OK)


def main():
    app.run(host="0.0.0.0", port=5150)


if __name__ == "__main__":
    main()
