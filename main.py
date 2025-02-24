from flask import Flask
from flask_restful import reqparse, Resource,Api, abort
import mysql.connector
db = mysql.connector.connect(host='YOUR_HOST', user='YOUR_USER_NAME', passwd='YOUR_PASSWORD', database='YOUR_DATA_BASE_NAME')
cr = db.cursor(dictionary=True)

app = Flask(__name__)
api = Api(app)


addvid = reqparse.RequestParser()
addvid.add_argument('name', type=str, required = True, help="you must enter a name")
addvid.add_argument('views', type=int, required = True, help="you must enter a views and it must be int")

class videos(Resource):
    
    def get(self, video_id):
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if not result:
            abort(404, message="the vid is not found")
        return result
    
    def put(self, video_id):
        args = addvid.parse_args()
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if result:
            abort (409, message = "the vid already exist")
        cr.execute(f"INSERT INTO `YOUR_TABLE` (`id`, `name`, `views`) VALUES ('{video_id}', '{args['name']}', '{args['views']}')")
        db.commit()
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        check = cr.fetchone()
        return check, 201
    def patch(self, video_id):
        args = addvid.parse_args()
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if not result:
            abort (404, message = "vid not found")
        cr.execute(f"UPDATE `YOUR_TABLE` SET  `name` = '{args['name']}', `views` = '{args['views']}' WHERE `YOUR_TABLE`.`id` = {video_id}")
        db.commit()
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        r = cr.fetchone()
        return r , 200
    def delete(self, video_id):
        cr.execute(f"SELECT * FROM `YOUR_TABLE` WHERE `id` = {video_id} ORDER BY `id` DESC")
        result = cr.fetchone()
        if not result:
            abort(404, message="the vid is not found")
        cr.execute(f"DELETE FROM YOUR_TABLE WHERE `YOUR_TABLE`.`id` = {video_id}")
        db.commit()
        return {"message" : "vid deleted succesfully"}, 200

api.add_resource(videos, '/vid/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)


    


