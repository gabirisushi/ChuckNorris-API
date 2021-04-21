from model import Joke

class Local:
  def __init__(self, db):
    self.db = db

  def search(self, query):
    filter_string = '%{}%'.format(query)
    jokes = Joke.query.filter(Joke.text.like(filter_string)).all()
    return jokes

  def create_joke(self, text, remote_id=None, deleted=False):
    joke = Joke(text = text, remote_id = remote_id, deleted = deleted)
    self.db.session.add(joke)
    self.db.session.commit()

    return {
      'id': joke.id,
      'text': joke.text,
      'remote_id': joke.remote_id
    }

  def update_joke_by_id(self, id, text):
    joke = Joke.query.get(id)
    joke.text = text
    self.db.session.commit()
    return self.get_joke_by_id(id)

  def get_joke_by_id(self, id):
    found = True
    response = Joke.query.get(id)

    if response is None:
      found = False
      joke = {}
    else:
      joke = {
      'id': response.id,
      'text': response.text,
      'remote_id': response.remote_id,
      'deleted': response.deleted
    }

    return found, joke

  def get_joke_by_remote_id(self, id):
    found = True
    response = Joke.query.filter(Joke.remote_id == id).first()

    if response is None:
      found = False
      joke = {}
    else:
      joke = {
      'id': response.id,
      'text': response.text,
      'remote_id': response.remote_id,
      'deleted': response.deleted
    }

    return found, joke

  def delete_joke_by_id(self, id):
    joke = Joke.query.get(id)

    if joke is None:
      return False
    joke.deleted = True
    self.db.session.commit()
    return True

  def check_local_existence_of_remote_ids(self, ids):
    jokes = Joke.query.filter(Joke.remote_id.in_(ids)).all()

    return [joke.remote_id for joke in jokes]
