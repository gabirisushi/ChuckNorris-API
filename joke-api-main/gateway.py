from model import Joke
from local import Local
from remote import Remote

class GateWay:
  def __init__(self, db):
    self.db = db
    self.local = Local(db)
    self.remote = Remote()

  def find_joke_by_id(self, id):
    found_locally = False
    if id[:5] == 'local':
      found, joke = self.local.get_joke_by_id(id[5:])
      found_locally = True
    else:
      found, joke = self.local.get_joke_by_remote_id(id)
      if found:
        found_locally = True
      else:
        found, joke = self.remote.by_id(id)
        joke['deleted'] = False

    return found, found_locally, joke

  def create_joke_locally(self, text, remote_id=None, deleted=False):

    return self.local.create_joke(text, remote_id=remote_id, deleted=deleted)

  def update_joke_by_id(self, id, text):
    found, found_locally, joke = self.find_joke_by_id(id)

    if joke['deleted']:
      return False, {}

    updated = False
    if found and found_locally:
      _, joke = self.local.update_joke_by_id(joke['id'], text)
      updated = True
    elif found:
      joke = self.local.create_joke(text, id)
      updated = True

    return updated, joke

  def delete_joke_by_id(self, id):
    found, found_locally, joke = self.find_joke_by_id(id)

    if joke['deleted']:
      return False, False


    if found and found_locally:
      status = self.local.delete_joke_by_id(joke['id'])
    elif found:
      self.create_joke_locally('', deleted=True, remote_id=joke['remote_id'])
      status = True
    else:
      status = False

    return found, status

  def search(self, query):
    local_jokes = [{'text': joke.text, 'id': joke.uid(), 'deleted': joke.deleted} for joke in self.local.search(query)]
    remote_jokes = [{'text': joke['text'], 'id': joke['remote_id']} for joke in self.remote.search(query)]

    jokes = []
    added_joke_ids = set()

    for joke in local_jokes:
      if joke['deleted']:
        added_joke_ids.add(joke['id'])
      elif joke['id'] not in added_joke_ids:
        jokes.append(joke)
        added_joke_ids.add(joke['id'])

    remote_ids = [joke['id'] for joke in remote_jokes]
    locally_existing_remote_ids = self.local.check_local_existence_of_remote_ids(remote_ids)
    [added_joke_ids.add(id) for id in locally_existing_remote_ids]

    for joke in remote_jokes:
      if joke['id'] not in added_joke_ids:
        jokes.append(joke)

    return jokes



    