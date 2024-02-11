from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained models
models = []
for i in range(1, 2):
    model = joblib.load(f'./modelo_random_forest_{i}.pkl')
    models.append(model)

# Endpoint to predict using the models
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the request data
        data = request.get_json()

        # Iterate over the models to make predictions for each one
        predictions = []
        for i, model in enumerate(models, start=1):
            # Assuming the request data contains features for prediction
            features = np.array(data['features'])

            # Make prediction using the model
            prediction = model.predict(features.reshape(1, -1))[0]
            predictions.append({'model': i, 'prediction': prediction})

        return jsonify(predictions), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
