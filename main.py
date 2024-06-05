# Importing all needed modules.
from flask import Flask, request, render_template
import pickle

# Loading the pipeline.
model = pickle.load(open("pipe.pkl", "rb"))

# Defining the label mapper.
label_mapper = {0 : "Bad", 1 : "Good"}

# Creating the app.
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def classify_fruit():
    if request.method == "GET":
        return render_template("index.html")
    else:
        # Extracting the values from form.
        size = request.form["size"]
        weight = request.form["weight"]
        sweetness = request.form["sweetness"]
        harvest_time = request.form["harvestTime"]
        ripeness = request.form["ripeness"]
        acidity = request.form["acidity"]

        # Making the prediction.
        X = [[size, weight, sweetness, harvest_time, ripeness, acidity]]
        y_pred = model.predict(X)[0]

        return render_template("index.html", prediction=label_mapper[y_pred])

app.run()
