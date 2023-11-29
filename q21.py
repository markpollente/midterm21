from flask import Flask, jsonify, request

app = Flask(__name__)

heart_rates = [
    {
        "heart_id": 1,
        "date" : "11/29/2023",
        "heart_rate" : "55",
    },
    {
        "heart_id": 2,
        "date" : "11/30/2023",
        "heart_rate" : "66",
    }
]

#1
@app.route('/heart_info', methods=["POST"])
def addHeartrate():
    heart_rate = request.get_json()
    heart_rates.append(heart_rate)
    return {'id': len(heart_rates)}, 200

#2
@app.route('/heart_info', methods=["Get"])
def getHeartrate():
    return jsonify(heart_rates)

#3
@app.route('/read_heart/<int:heart_id>', methods=["GET"])
def getSpecificHeartrate(heart_id):
    return jsonify({
        "heart_id": next((item["heart_id"] for item in heart_rates if item['heart_id'] == heart_id), None),
        "date": next((item["date"] for item in heart_rates if item['heart_id'] == heart_id), None),
        "heart_rate": next((item["heart_rate"] for item in heart_rates if item['heart_id'] == heart_id), None)
    })

#4

#5
@app.route('/heart_info/<int:heart_id>', methods=["DELETE"])
def deleteHeartrate(heart_id):
    heart_rates.pop(heart_id)
    return "The heart rate has been deleted", 200


if __name__ == '__main__':
    app.run()