from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)


@app.post("/api/<deviceName>")
def handle(deviceName):
    print(deviceName)
    params = [str(deviceName)]
    subprocess.run(['bash', 'hello.sh'] + params)

    return jsonify({
        "message": "ok"
    })


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)