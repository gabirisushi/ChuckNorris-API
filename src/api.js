import axios from 'axios'

const baseURL = 'http://127.0.0.1:5000/api/jokes/'
const headers = {
  'Content-Type': 'application/json'
}

export default {
  get_jokes_by_query: (query, callback, failCallback=console.log) => {
    const url = baseURL + '?query=' + query
    axios.get(url).then(callback).catch(failCallback)
  },

  delete_joke_by_id: (id, callback, failCallback=console.log) => {
    const url = baseURL + id
    axios.delete(url).then(callback).catch(failCallback)
  },

  editJokeById: (id, text, callback, failCallback=console.log) => {
    const url = baseURL + id
    axios.put(url, { text }).then(callback).catch(failCallback)
  },

  getJokeByID: (id, callback, failCallback=console.log) => {
    const url = baseURL + id
    axios.get(url).then(callback).catch(failCallback)
  },

  createJoke: (text, callback, failCallback=console.log) => {
    const url = 'http://127.0.0.1:5000/api/jokes'
    axios.post(url, { text }, { headers }).then(callback).catch(failCallback)
  }
}