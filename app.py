from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "https://tejaschoukale.github.io"}})

# Allow CORS for POST and OPTIONS methods
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    header['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Load the pre-trained linear regression model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return "Server is running bro"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    app.logger.info(f"Received data: {data}")  # Log received data
    if 'features' not in data:
        app.logger.error("Missing 'features' data in request")
        return jsonify({'error': 'Missing or invalid data'}), 400

    features = np.array(data['features']).reshape(1, -1)
    app.logger.info(f"Features for prediction: {features}")  # Log features for prediction
    prediction = model.predict(features)
    app.logger.info(f"Prediction: {prediction}")  # Log prediction
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
