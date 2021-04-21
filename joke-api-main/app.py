from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
from model import db
from gateway import GateWay

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///joke.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

gateway = GateWay(db)

@app.route('/api/jokes', methods=['POST'])
@cross_origin()
def create_joke():
  data = request.get_json()
  joke = gateway.create_joke_locally(data['text'])

  result_id = joke['remote_id'] if joke['remote_id'] is not None else 'local' + str(joke['id'])

  return {
    'id': result_id,
    'text': joke['text']
  }

@app.route('/api/jokes/<id>', methods=['GET'])
@cross_origin()
def get_joke_by_id(id):
  found, _found_locally, joke = gateway.find_joke_by_id(id)

  if found and not joke['deleted']:
    result_id = joke['remote_id'] if joke['remote_id'] is not None else 'local' + str(joke['id'])

    return {
      'id': result_id,
      'text': joke['text']
    }
  else:
    abort(404)

@app.route('/api/jokes/<id>', methods=['PUT'])
@cross_origin()
def edit_joke_by_id(id):
  data = request.get_json()
  text = data['text']

  updated, joke = gateway.update_joke_by_id(id, text)

  if not updated:
    abort(404)
  else:
    result_id = joke['remote_id'] if joke['remote_id'] is not None else 'local' + str(joke['id'])

    return {
      'id': result_id,
      'text': joke['text']
    }

@app.route('/api/jokes/<id>', methods=['DELETE'])
@cross_origin()
def delete_joke_by_id(id):
  found, deleted = gateway.delete_joke_by_id(id)

  if found:
    return {
      'id': id,
      'deleted': deleted
    }
  else:
    abort(404)

@app.route('/api/jokes/', methods=['GET'])
@cross_origin()
def search():
  query = request.args.get('query')

  jokes = [{'text': joke['text'], 'id': joke['id']} for joke in gateway.search(query)]

  return {'jokes': jokes}