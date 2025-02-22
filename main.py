from flask import Flask
from flask_restful import reqparse, Resource,Api, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    views = db.Column(db.Integer, nullable=False)

jsonify = {
    'name' : fields.String(),
    'views' : fields.Integer(),
    'id' : fields.Integer()
}
addvid = reqparse.RequestParser()
addvid.add_argument('name', type=str, required = True, help="you must enter a name")
addvid.add_argument('views', type=int, required = True, help="you must enter a views and it must be int")

class videos(Resource):
    
    @marshal_with(jsonify)
    def get(self, video_id):
        result = model.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="the vid is not found")
        return result
    
    @marshal_with(jsonify)
    def put(self, video_id):
        args = addvid.parse_args()
        result = model.query.filter_by(id=video_id).first()
        if result:
            abort (409, message = "the vid already exist")
        vid = model(id = video_id, name = args['name'], views = args['views'])
        db.session.add(vid)
        db.session.commit()
        check = model.query.filter_by(id=video_id).first()
        return check, 201

api.add_resource(videos, '/vid/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)


    


