document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('prediction-form').addEventListener('submit', function(event) {
        event.preventDefault();

        // Fetch the value of 'years' input field
        var years = document.getElementById('years').value;

        // Construct the request payload with 'years' key
        var payload = {
            'years': years
        };

        // Send a POST request to the Flask server with the constructed payload
        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            mode: 'cors' // Add this line for CORS
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to predict salary');
            }
            return response.json();
        })
        .then(data => {
            console.log('Prediction result:', data.prediction);
            // Handle the prediction result
            var predictionResult = document.getElementById('prediction-result');
            predictionResult.innerHTML = '<p>Predicted salary: $' + data.prediction + '</p>';
            // You can update your UI or display the prediction result here
        })
        .catch(error => {
            console.error('Error:', error.message);
            // Handle errors, such as displaying an error message to the user
        });
    });
});
