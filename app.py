from flask import Flask, request, jsonify

import mlib

app = Flask(__name__)

@app.route("/")
def home():
    html = "<h3>Predict the cluster of an user</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Predicts the Height of MLB Players"""
    
    json_payload = request.json

    data_to_predict = {
        'Monto activo': json_payload['monactivo'], 
        'Promedio Ventas': json_payload['meansales'], 
        'Promedio Cesiones': json_payload['meancesiones'], 
        'proyeccion ventas': json_payload['proyecsales'], 
        'proyeccion compras': json_payload['proyecbuys']}

    prediction = mlib.predict(data_to_predict)
    return jsonify({'Cluster': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)