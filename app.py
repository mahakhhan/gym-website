from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/membership")
def membership():
    # Dynamic membership plans
    plans = [
        {"name": "Basic", "duration": "1 Month", "price": "Rs. 5,000"},
        {"name": "Standard", "duration": "3 Months", "price": "Rs. 13,000"},
        {"name": "Premium", "duration": "6 Months", "price": "Rs. 25,000"}
    ]
    return render_template("membership.html", plans=plans)

if __name__ == "__main__":
    app.run(debug=True)
