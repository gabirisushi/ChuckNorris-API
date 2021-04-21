
from requests import get

BASE_URL = 'https://api.chucknorris.io/jokes/'

class Remote:
  def by_id(self, id):
    url = BASE_URL + id
    found = True
    try:
      result = get(url).json()
      joke = {'remote_id': result['id'], 'text': result['value']}
    except Exception as _exception:
      joke = {}
      found = False
    
    return found, joke

  def search(self, query):
    url = BASE_URL + 'search?query=' + query
    try:
      results = get(url).json()['result']
      jokes = [{'remote_id': result['id'], 'text': result['value']} for result in results]
    except Exception as _exception:
      jokes = []

    return jokes
    