import os
import tempfile

import pytest
from mock import patch

from app import app, db
from model import Joke
from remote import Remote


@pytest.fixture
def client():
  if os.path.exists('test.db'):
    os.remove('test.db')

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['TESTING'] = True

  with app.test_client() as client:
    with app.app_context():
        db.create_all()
    yield client

def test_post_joke(client):
  ''' Posting a joke will return the joke text along with a local id'''

  rv = client.post('/api/jokes', json={'text':'hello world'})
  assert 'hello world' == rv.json['text']
  assert rv.json['id'][:5] == 'local'


def test_get_locally_available_joke_by_id(client):
  post_response = client.post('/api/jokes', json={'text':'this is a joke'}).json
  id = post_response['id']

  get_response = client.get('/api/jokes/{}'.format(id)).json

  assert get_response['text'] == 'this is a joke'

def test_get_remote_joke_by_id(client):
  with patch.object(Remote, 'by_id') as mocked_remote_request_function:
    mocked_remote_request_function.return_value = (True, {'text': 'Chuck Norris joke', 'remote_id': 'Abf3v_'})
  
    get_response = client.get('/api/jokes/Abf3v_').json

    assert get_response['text'] == 'Chuck Norris joke'
    
def test_edit_locally_available_joke(client):
  # First we create a joke
  post_response = client.post('/api/jokes', json={'text':'this is a joke'}).json
  id = post_response['id']
  get_response = client.get('/api/jokes/{}'.format(id)).json
  assert get_response['text'] == 'this is a joke'

  # Now edit the joke
  put_response = client.put('/api/jokes/{}'.format(id), json={'text':'this is another joke'}).json

  # Now we get the edited joke
  get_response = client.get('/api/jokes/{}'.format(id)).json

  assert(get_response['text'] == 'this is another joke')

def test_edit_remote_joke(client):
  with patch.object(Remote, 'by_id') as mocked_remote_request_function:
    mocked_remote_request_function.return_value = (True, {'text': 'Chuck Norris joke', 'remote_id': 'Abf3v_'})

    # We edit the remote joke
    put_response = client.put('/api/jokes/{}'.format('Abf3v_'), json={'text':'this is another joke'}).json

    # Then get and assert that for the same id, the updated joke is received
    get_response = client.get('/api/jokes/{}'.format('Abf3v_')).json
    assert(get_response['text'] == 'this is another joke')

def test_delete_locally_available_joke(client):
  # First we create a joke
  post_response = client.post('/api/jokes', json={'text':'this is a joke'}).json
  id = post_response['id']
  get_response = client.get('/api/jokes/{}'.format(id)).json
  assert get_response['text'] == 'this is a joke'

  # Now delete the joke
  delete_response = client.delete('/api/jokes/{}'.format(id)).json

  # Now we try to get the deleted joke
  get_response = client.get('/api/jokes/{}'.format(id))

  assert(get_response.status_code == 404)

def test_delete_remote_joke(client):
  with patch.object(Remote, 'by_id') as mocked_remote_request_function:
    mocked_remote_request_function.return_value = (True, {'text': 'Chuck Norris joke', 'remote_id': 'Abf3v_'})

    # We remove the remote joke
    delete_response = client.delete('/api/jokes/{}'.format('Abf3v_'))

    # Then get and assert that for the same id, 404 is returned
    get_response = client.get('/api/jokes/{}'.format('Abf3v_'))
    assert(get_response.status_code == 404)

def test_get_jokes_by_query(client):
  # We patch the Remote class to return a chuck norris bomb joke
  with patch.object(Remote, 'search') as mocked_remote_request_function:
    mocked_remote_request_function.return_value = [{'text': 'Chuck Norris bomb joke', 'remote_id': 'Abf3v_'}]

  # We create some sample local jokes and a remote joke
    local_jokes = [
      'Bombs are scared of chuck norris',
      'chuck norris throws a bomb and kills 5 people, then it explodes',
      'chuck norris can make guns using lego'
    ]

    for joke in local_jokes:
      client.post('/api/jokes', json={'text':joke})



    # query jokes containing the word 'bomb'
    get_response = client.get('/api/jokes/?query=bomb').json
    print(get_response)
    obtained_jokes = [joke['text'] for joke in get_response['jokes']]

    # Notice that we're only testing the first two jokes as the third joke does not contain 'bomb'
    for joke in local_jokes[:2]:
      assert joke in obtained_jokes
    
    assert 'Chuck Norris bomb joke' in obtained_jokes
