from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "my world is going to change little with all positive things in the world"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)