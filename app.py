from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.get("/api/<deviceName>")
def handle(deviceName):
    print(deviceName)
    params = [str(deviceName)]
    subprocess.run(['bash', '/home/pham_hoang/Desktop/python/hello.sh'] + params)

    return jsonify({
        "message": "ok"
    })
