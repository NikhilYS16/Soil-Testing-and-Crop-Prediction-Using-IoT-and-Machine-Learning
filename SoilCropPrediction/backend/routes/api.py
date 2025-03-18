from flask import Blueprint, request, jsonify
import joblib, json
from utils.preprocess import preprocess_data

# Define the blueprint for the crop prediction
crop_prediction = Blueprint('crop_prediction', __name__)

# Load the saved model
model = joblib.load('C:\\SoilCropPrediction\\backend\\model\\crop_model.pkl')

# Load the crop information
with open('C:\\SoilCropPrediction\\backend\\data\\crop_info.json') as f:
    CROP_INFO = json.load(f)

@crop_prediction.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.json  # Expecting {"N": ..., "P": ..., "K": ..., etc.}

        # Validate the presence of required fields
        required_fields = ['N', 'P', 'K', 'temperature', 'ph', 'rainfall']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing input data"}), 400

        # Preprocess the input data
        features = preprocess_data(data)

        # Make a prediction
        predictions = model.predict([features])[0]

        # Retrieve crop details
        crop_details = CROP_INFO.get(predictions, {"description": "No information available."})

        # Send back the prediction result
        return jsonify({
            'predicted_crop': predictions,
            "crop_details": crop_details
            })

    except KeyError as e:
        return jsonify({"error": f"Missing data field: {e}"}), 400

    except Exception as e:
        # Catch any errors and send an error message back
        return jsonify({"error": str(e)}), 500
