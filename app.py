from flask import Flask, request, jsonify
import os
from service import Handler

app = Flask(__name__)

handler = Handler()


@app.post("/api/<deviceName>/inactivity")
def handle_inactivity(deviceName):
    print("inactivity deviceName: %s", deviceName)

    container_name = detect_container_name(deviceName)
    if container_name is not None:
        handler.push_data(container_name)

    return jsonify({
        "message": "ok"
    })


@app.post("/api/<deviceName>/activity")
def handle_activity(deviceName):
    print("activity deviceName: %s", deviceName)

    return jsonify({
        "message": "ok"
    })


def detect_container_name(device_name):
    if "HK" in str(device_name):
        return detect_container_ns3_valve(device_name)

    if "BTW" in str(device_name):
        return detect_container_btw(device_name)

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


def detect_container_btw(btw_device_name):
    tb_gateway_btw_1 = [
        "BTW_0001", "BTW_0002", "BTW_0004", "BTW_0005", "BTW_0008", "BTW_0009", "BTW_0010", "BTW_0111", "BTW_0141",
        "BTW_0211", "BTW_0221", "BTW_0231", "BTW_0232", "BTW_0241", "BTW_0251", "BTW_0261", "BTW_0262", "BTW_0271",
        "BTW_0272", "BTW_0281", "BTW_0282", "BTW_0291"
    ]

    tb_gateway_btw_2 = [
        "BTW_0311", "BTW_0321", "BTW_0331", "BTW_0332", "BTW_0351", "BTW_0411", "BTW_0414", "BTW_0421", "BTW_0431",
        "BTW_0441", "BTW_0451", "BTW_0452", "BTW_0461", "BTW_0491", "BTW_0511", "BTW_0521", "BTW_0531", "BTW_0541",
        "BTW_0611", "BTW_0621", "BTW_0631", "BTW_0641"
    ]

    tb_gateway_btw_3 = [
        "BTW_0651", "BTW_0652", "BTW_0661", "BTW_0711", "BTW_0721", "BTW_0731", "BTW_0741", "BTW_0811", "BTW_0821",
        "BTW_0831", "BTW_1001", "BTW_1002", "BTW_1003", "BTW_1004", "BTW_1005", "BTW_1006", "BTW_1007", "BTW_1008",
        "BTW_1009", "BTW_1010", "BTW_1011", "BTW_1012"
    ]

    tb_gateway_btw_4 = [
        "BTW_1013", "BTW_1014", "BTW_1015", "BTW_1016", "BTW_1017", "BTW_1018", "BTW_1341", "BTW_2001", "BTW_2002",
        "BTW_2610", "BTW_2611", "BTW_3111", "BTW_3121"
    ]

    if str(btw_device_name) in tb_gateway_btw_1:
        return "tb_gateway_btw_1"
    if str(btw_device_name) in tb_gateway_btw_2:
        return "tb_gateway_btw_2"
    if str(btw_device_name) in tb_gateway_btw_3:
        return "tb_gateway_btw_3"
    if str(btw_device_name) in tb_gateway_btw_4:
        return "tb_gateway_btw_4"

    return None


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6000))
    app.run(debug=True, host='0.0.0.0', port=port)
