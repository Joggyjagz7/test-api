# 📘 How to Use This CodeSandbox

This project contains a Python script that makes a `POST` request to the [Me-Cash API](https://api.me-cash.com/v1/quote). Follow the steps below to run it successfully.

---

## 🛠 Prerequisites

Make sure the sandbox environment is running and that you're using the **Devbox (Python)** template.

---

## 📄 Files

- **`meCash-requests.py`** – The main Python script that sends a request to the Me-Cash API.
- **`requirements.txt`** – Contains required Python packages (currently only `requests`).

---

## ▶️ How to Run

1. **Open the Terminal**  
   Go to the bottom panel and select the `TERMINAL` tab.  
   Or open a new one via the sidebar "+" ➜ "New Terminal".

2. **Install dependencies** (only if not already installed)
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script**
   ```bash
   python meCash-request.py
   ```
This will execute the script and send a POST request to the Me-Cash API using the provided headers and body data.

4. **Expected Output**
You should see two things printed in the terminal:
- The HTTP status code (e.g., 200 for success, 400 for a bad request).
- The response body from the Me-Cash API, usually in JSON format.


