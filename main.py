from flask import *
import json

app = Flask(__name__)

@app.route("/")
def home():
    dataSet = {
        "page": "home",
        "message": "hello world"
    }
    jsonDumb = json.dumps(dataSet)
    return jsonDumb
@app.route("/user/")
def user():
    userQuery = str(request.args.get("user"))
    dataSet = {
        "main user is": f"{userQuery}",
        "message": "hello world"
    }
    jsonDumb = json.dumps(dataSet)
    return jsonDumb


if __name__ == "__main__":
    app.run(debug=True)