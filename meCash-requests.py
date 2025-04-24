import requests  # Import the requests library for making HTTP requests

# Set the API endpoint URL e.g https://api.mec-cash.com/v1/quotes
url = "https://{{baseURL}}/v1/"

# Set the headers including content type and API key for authorization
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "YOUR_API_KEY"  # Replace with your actual API key
}

# Define the data payload to be sent in the POST request
data = {
    "paymentChannel": "",  # Specify the payment channel if required
    "source": {
        "amount": 1,        # Amount to be transferrde
        "country": "",      # Source country code (e.g., "US")
        "currency": ""      # Source currency code (e.g., "USD")
    },
    "target": {
        "country": "",      # Target country code
        "currency": ""      # Target currency code
    }
}

# Send the POST request to the API with headers and JSON data
response = requests.post(url, headers=headers, json=data)

# Print the HTTP response status code and response body
print(response.status_code)
print(response.text)
