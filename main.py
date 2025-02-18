from flask import *
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
api = Api(app)

videoArgs = reqparse.RequestParser()
videoArgs.add_argument("name", type=str, help="enter a name")
videoArgs.add_argument("likes", type=int, help="enter a num")
videoArgs.add_argument("views", type=int, help="enter a num")

class putreq(Resource):
    def put(self, videoID):
        args = videoArgs.parse_args()
        return {videoID : args}
api.add_resource(putreq, "/video/<int:videoID>")

if __name__ == "__main__":
    app.run(debug=True)