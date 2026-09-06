from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# ⭐ Dashboard route (your main app logic)
@app.route("/dashboard")
def dashboard():
    # Load crypto data from CSV
    data = pd.read_csv("crypto_data.csv")
    return render_template("index.html", data=data)

# ⭐ Health check route (fixes Render HEAD error)
@app.route("/", methods=["GET", "HEAD"])
def home():
    return "Crypto Dashboard is running!"

# ⭐ Optional: dedicated health endpoint (best practice)
@app.route("/health", methods=["GET", "HEAD"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
