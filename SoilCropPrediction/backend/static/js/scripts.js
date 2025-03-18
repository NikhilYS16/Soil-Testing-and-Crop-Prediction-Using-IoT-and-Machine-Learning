function predictCrop() {
    const data = {
        N: parseFloat(document.getElementById('nitrogen').value),
        P: parseFloat(document.getElementById('phosphorus').value),
        K: parseFloat(document.getElementById('potassium').value),
        temperature: parseFloat(document.getElementById('temperature').value),
        ph: parseFloat(document.getElementById('ph').value),
        rainfall: parseFloat(document.getElementById('rainfall').value)
    };

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.predicted_crop) {
            document.getElementById('result').style.display = 'block';
            document.getElementById('result').textContent = `Predicted Crop: ${result.predicted_crop}`;
            showRecommendation(result.predicted_crop);
        } else {
            document.getElementById('result').style.display = 'block';
            document.getElementById('result').textContent = 'Error: Could not fetch prediction.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').style.display = 'block';
        document.getElementById('result').textContent = 'Error: Could not connect to server.';
    });
}

// Show recommendation for the predicted crop
function showRecommendation(predictedCrop) {
    let recommendations = {
        "wheat": "Wheat is a staple crop and requires moderate rainfall and cool temperature for optimal growth.",
        "rice": "Rice grows best in warm, wet environments and is highly water-dependent.",
        "maize": "Maize needs a warm climate and good sunlight; it’s sensitive to frost.",
        "orange": "Oranges require warm temperatures, ample sunlight, and moderate water.",
        // Add more crop recommendations as needed
    };

    document.getElementById('recommendation').style.display = 'block';
    document.getElementById('recommendation').textContent = `Recommendation for ${predictedCrop}: ${recommendations[predictedCrop] || "No specific recommendation available."}`;
}
