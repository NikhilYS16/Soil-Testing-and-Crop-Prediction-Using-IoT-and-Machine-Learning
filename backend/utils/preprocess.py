# backend/utils/preprocess.py

def preprocess_data(data):
    """
    Perform any necessary data preprocessing.
    For example, scale or normalize the input values if required.
    """
    # Assuming data is a dictionary of inputs
    # e.g., {'N': 50, 'P': 40, 'K': 35, 'temperature': 25, 'ph': 6.5, 'rainfall': 100}

    # Example normalization (if required by your model)
    data['N'] = data['N'] / 100
    data['P'] = data['P'] / 100
    data['K'] = data['K'] / 100
    data['temperature'] = data['temperature'] / 50  # assuming max temperature = 50
    data['ph'] = data['ph'] / 14  # assuming ph scale of 0-14
    data['rainfall'] = data['rainfall'] / 200  # assuming max rainfall = 200mm

    return list(data.values())  # Returns a list of values for prediction input
