from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

# Initialize the scaler (assuming you've saved your scaler parameters)
scaler = StandardScaler()

# Dummy fit for scaler (replace with actual values or load pre-fitted scaler)
dummy_data = np.array([[0, 1, 2, 3, 4, 5]])
scaler.fit(dummy_data)

@app.route('/')
def index():
    return 'Welcome to the prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(f"Received data: {data}")

    try:
        # Extract and convert inputs
        time_spent = float(data.get('Time Spent (sec)', None))
        question_difficulty = int(data.get('Question Difficulty', None))
        total_questions_answered = int(data.get('Total Questions Answered', None))
        correct_answers = int(data.get('Correct Answers', None))
        score = float(data.get('Score (%)', None))
        quiz_duration = float(data.get('Quiz Duration (sec)', None))

        # Handle missing keys or invalid types
        if None in [time_spent, question_difficulty, total_questions_answered, correct_answers, score, quiz_duration]:
            return jsonify({"error": "Missing or invalid input data"}), 400

        # Apply custom logic for prediction
        if time_spent < 15 and score < 80:
            prediction_result = 'Less Prepared'
        elif time_spent >= 15 and score > 80:
            prediction_result = 'Less Prepared'
        else:
            prediction_result = 'Well Prepared'

        # Print the prediction result
        print(f'Prediction result: {prediction_result}')

        # Return JSON response with prediction result
        return jsonify({"prediction": prediction_result})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": "An error occurred during prediction"}), 500

if __name__ == '__main__':
    app.run(debug=True)
