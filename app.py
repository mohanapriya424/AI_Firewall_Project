from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__)
model = joblib.load("firewall_model.pkl")
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        packet_size = int(request.form["packet_size"])
        request_rate = int(request.form["request_rate"])
        failed_logins = int(request.form["failed_logins"])
        data = pd.DataFrame(
            [[packet_size, request_rate, failed_logins]],
            columns=["packet_size", "request_rate", "failed_logins"]
        )
        prediction = model.predict(data)
        if prediction[0] == 1:
            result = "Attack Detected"
        else:
            result = "Safe Traffic"
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)