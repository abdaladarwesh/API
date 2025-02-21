from flask import *
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
videoArgs = reqparse.RequestParser()
videoArgs.add_argument("name", type=str, help='this is name')
videoArgs.add_argument('likes', type=int, help='this is likes')


class helloWorld(Resource):
    def get(self): 
        return {'message':'hello world'}

class addvids(Resource):
    def put(self):
        args = videoArgs.parse_args()
        return {'1':args}

api.add_resource(addvids, "/vid")
api.add_resource(helloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)