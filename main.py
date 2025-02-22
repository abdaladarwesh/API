from flask import Flask
from flask_restful import reqparse, Resource,Api, abort, fields, marshal_with
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', passwd='', database='videos')
cr = db.cursor(dictionary=True)

app = Flask(__name__)
api = Api(app)


addvid = reqparse.RequestParser()
addvid.add_argument('name', type=str, required = True, help="you must enter a name")
addvid.add_argument('views', type=int, required = True, help="you must enter a views and it must be int")

class videos(Resource):
    
    def get(self, video_id):
        cr.execute(f"SELECT * FROM `vids` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if not result:
            abort(404, message="the vid is not found")
        return result
    
    def put(self, video_id):
        args = addvid.parse_args()
        cr.execute(f"SELECT * FROM `vids` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if result:
            abort (409, message = "the vid already exist")
        cr.execute(f"INSERT INTO `vids` (`id`, `name`, `views`) VALUES ('{video_id}', '{args['name']}', '{args['views']}')")
        db.commit()
        cr.execute(f"SELECT * FROM `vids` WHERE `id` = {video_id} ORDER BY `id` DESC")
        check = cr.fetchone()
        return check, 201

api.add_resource(videos, '/vid/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)


    


