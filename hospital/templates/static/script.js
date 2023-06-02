document.getElementById('patient-form').addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent form submission

  const input = document.getElementById('data-input').value;

  // Send a POST request to the backend endpoint
  fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      data: input
    })
  })
    .then(response => response.json())
    .then(data => {
      // Display the prediction results
      const resultsDiv = document.getElementById('result-container');
      resultsDiv.innerText = 'Predictions: ' + data.predictions.join(', ');
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
