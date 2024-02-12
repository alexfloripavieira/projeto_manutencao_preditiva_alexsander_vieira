from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained models
def load_model(model_number):
    model = joblib.load(f'./modelos/modelo_random_forest_{model_number}.pkl')
    return model

# Endpoint to predict using the models
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the request data
        data = request.get_json()

        # Get the model number and features from the request data
        model_number = data['model_number']
        features_list = data['features']

        # Load the specified model
        model = load_model(model_number)

        # Make prediction using the model
        features = np.array(features_list)
        prediction = model.predict(features.reshape(1, -1))[0]

        return jsonify({'model': model_number, 'prediction': prediction}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
