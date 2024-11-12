from flask import Flask, render_template, request
app = Flask(__name__)

# Predefined exchange rates for simplicity
exchange_rates = {
    "USD": {"INR": 84.5, "EUR": 0.94, "PND":0.78, "CAD":1.39, "YEN":153.37},
    "INR": {"USD": 0.012, "EUR": 0.011, "PND": 0.0092, "CAD":0.016, "YEN":1.82 },
    "EUR": {"USD": 1.06, "INR": 88.0, "PND": 164.25 , "CAD":1.49 , "YEN":164.22},
    "PND": {"USD": 1.29, "INR": 108.88, "EUR": 1.21, "CAD":1.80, "YEN":198},
    "YEN": {"USD": 0.0065, "INR": 0.55, "EUR": 0.0061,"PND":0.0051,"CAD":0.0091},
    "CAD": {"USD": 0.71, "INR": 60.61, "EUR": 0.67, "PND":0.55, "YEN":110.35},
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    from_currency = "INR"
    to_currency = "USD"
    amount = 0

    if request.method == "POST":
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]
        amount = float(request.form["amount"])
        
        # Calculate converted amount
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            converted_amount = amount * exchange_rates[from_currency][to_currency]
            result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            result = "Conversion rate not available."

    currencies = list(exchange_rates.keys())
    return render_template("index.html", currencies=currencies, result=result,
                           from_currency=from_currency, to_currency=to_currency, amount=amount)

if __name__ == "__main__":
    app.run(debug=True)