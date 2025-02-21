from flask import Flask
from flask_restful import reqparse, Resource,Api, abort

app = Flask(__name__)
api = Api(app)

addVids = reqparse.RequestParser()
addVids.add_argument("name", type=str, required=True,  help='name type is not right or its requierd')
addVids.add_argument("views", type=int, required=True,  help='views type is not right or its requierd')

videos = {}
def check(video_id):
    if video_id not in videos:
        abort(404, message="the video you request is not exsit......")

def checkForExsit(video_id):
    if video_id in videos:
        abort(409, message="the video you request to put is already exsit......")

class vids(Resource):
    def get(self, video_id):
        check(video_id)
        return videos[video_id] , 200
    
    def put(self, video_id):
        checkForExsit(video_id)
        args = addVids.parse_args()
        videos[video_id] = args
        return videos[video_id] , 201
    
    def delete (self, video_id):
        check(video_id)
        del videos[video_id]
        return '', 204
    
    
api.add_resource(vids, "/vid/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)