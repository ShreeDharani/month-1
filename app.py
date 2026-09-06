from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

def load_data():
    df = pd.read_csv("crypto_data.csv")
    df = df.tail(20)
    return df.to_dict(orient="records")

@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", data=data)

@app.route("/chart-data")
def chart_data():
    df = pd.read_csv("crypto_data.csv")
    df = df.tail(50)

    return jsonify({
        "labels": df["Timestamp"].tolist(),
        "prices": df["Price"].str.replace("$", "").str.replace(",", "").astype(float).tolist(),
        "names": df["Name"].tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)
