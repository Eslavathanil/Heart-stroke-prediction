from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hm.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the data from the request
        data = request.get_json()

        # Convert input data to a list of floats/integers for model prediction
        features = [
            int(data['age']),
            int(data['sex']),
            int(data['cp']),
            float(data['trestbps']),
            float(data['chol']),
            int(data['fbs']),
            int(data['restecg']),
            float(data['thalach']),
            int(data['exang']),
            float(data['oldpeak']),
            int(data['slope']),
            int(data['ca']),
            int(data['thal'])
        ]

        # Placeholder for model prediction
        # Replace with actual model logic here
        prediction = np.random.choice([0, 1])  # Simulate prediction

        # Respond with the prediction
        return jsonify({'prediction': 'Heart Disease Present' if prediction == 1 else 'No Heart Disease'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
