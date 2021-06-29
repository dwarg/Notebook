from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    desc = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __repr__(self):
        return f"{self.id}"


db.create_all()


class Schema(ModelSchema):
    class Meta:
        fields = ("id", "title", "desc", "createdAt", "updated_at")
        model = Notebook
        sqla_session = db.session


@app.route("/api/add_note", methods=['POST'])
def add_hit():
    data = {
        'title': 'Example titlel',
        'desc': 'Description'
    }
    post_schema = Schema(
        only=['title', 'desc', 'createdAt'])
    post = post_schema.load(data)
    result = post_schema.dump(post.create())
    return make_response(jsonify({"Notebook": result}), 200)


@app.route('/api/note', methods=['POST'])
def method_post():
    data = request.get_json()
    post_schema = Schema(
        only=['title', 'desc', 'createdAt'])
    post = post_schema.load(data)
    result = post_schema.dump(post.create())
    return make_response(jsonify({"Notebook": result}), 200)


@app.route('/api/note', methods=['GET'])
def method_get():
    get = Notebook.query.all()
    get_schema = Schema(
        many=True, only=['id', 'title', 'desc'])
    result = get_schema.dump(get)
    return make_response(jsonify({"Notebook": result}))


@app.route('/api/note/<id>', methods=['GET'])
def method_get_by_id(id):
    get_by_id = Notebook.query.get(id)
    get_schema = Schema(
        only=['id', 'title', 'desc', 'createdAt'])
    result = get_schema.dump(get_by_id)
    return make_response(jsonify({"Notebook": result}))


@app.route('/api/note/<id>', methods=['PUT'])
def method_put(id):
    data = request.get_json()
    put_by_id = Notebook.query.get(id)

    if data.get('title'):
        put_by_id.title = data['title']
    if data.get('desc'):
        put_by_id.desc = data['desc']

    db.session.add(put_by_id)
    db.session.commit()

    put_schema = Schema(
        only=['title', 'desc', 'updated_at'])
    result = put_schema.dump(put_by_id)
    return make_response(jsonify({"Notebook": result}))


@app.route('/api/note/<id>', methods=['DELETE'])
def method_delete(id):
    del_by_id = Notebook.query.get(id)
    db.session.delete(del_by_id)
    db.session.commit()
    return make_response("", 204)
