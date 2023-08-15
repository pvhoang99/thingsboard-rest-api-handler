from flask import Flask, request, jsonify
import os
from service import Handler

app = Flask(__name__)

handler = Handler()


@app.post("/api/<deviceName>/inactivity")
def handle(deviceName):
    print("inactivity deviceName: %s", deviceName)

    container_name = detect_container_name(deviceName)
    if container_name is not None:
        handler.push_data(container_name)

    return jsonify({
        "message": "ok"
    })


@app.post("/api/<deviceName>/activity")
def handle(deviceName):
    print("activity deviceName: %s", deviceName)

    return jsonify({
        "message": "ok"
    })


def detect_container_name(device_name):
    if "HK" in str(device_name):
        return detect_container_ns3_valve(device_name)

    return None


def detect_container_ns3_valve(ns3_valve_device_name):
    tb_gateway_ns3_valve_1 = [
        'HK01', 'HK02', 'HK03', 'HK04', 'HK05', 'HK06', 'HK07', 'HK08', 'HK09', 'HK10'
    ]
    tb_gateway_ns3_valve_2 = [
        'HK11', 'HK12', 'HK13', 'HK14', 'HK15', 'HK16', 'HK17', 'HK18', 'HK19', 'HK20'
    ]
    tb_gateway_ns3_valve_3 = [
        'HK21', 'HK22', 'HK23', 'HK24', 'HK25', 'HK26', 'HK27', 'HK28', 'HK29', 'HK30'
    ]
    tb_gateway_ns3_valve_4 = [
        'HT', 'HK32', 'HM', 'HK35', 'HK36'
    ]

    if str(ns3_valve_device_name) in tb_gateway_ns3_valve_1:
        return "tb_gateway_ns3_valve_1"

    if str(ns3_valve_device_name) in tb_gateway_ns3_valve_2:
        return "tb_gateway_ns3_valve_2"

    if str(ns3_valve_device_name) in tb_gateway_ns3_valve_3:
        return "tb_gateway_ns3_valve_3"

    if str(ns3_valve_device_name) in tb_gateway_ns3_valve_4:
        return "tb_gateway_ns3_valve_4"

    return None


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
