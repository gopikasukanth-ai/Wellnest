from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/flashcards")
def flashcards():
    return render_template("flashcards.html")

@app.route("/meal-planner")
def meal_planner():
    return render_template("meal_planner.html")

@app.route("/food-scanner")
def food_scanner():
    return render_template("food_scanner.html")

@app.route("/food-swaps")
def food_swaps():
    return render_template("food_swaps.html")

@app.route("/dietary-preferences")
def dietary_preferences():
    return render_template("dietary_preferences.html")

@app.route("/nutrition-chat")
def nutrition_chat():
    return render_template("nutrition_chat.html")

@app.route("/tracking-analytics")
def tracking_analytics():
    return render_template("tracking_analytics.html")

@app.route("/nutrition-content")
def nutrition_content():
    return render_template("nutrition_content.html")

@app.route("/specialized-features")
def specialized_features():
    return render_template("specialized_features.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)