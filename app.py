from flask import Flask, render_template, jsonify
from read_data import get_planet_data

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

data = get_planet_data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    return jsonify(data)

if __name__ == "__main__":
    app.run()