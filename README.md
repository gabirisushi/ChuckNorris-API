![image](https://forthebadge.com/images/badges/made-with-python.svg) ![image](https://forthebadge.com/images/badges/kinda-sfw.svg)
# Hello Hello! Please go to the bottom of the Readme for some instructions and specifications about my work!

![image](https://media.giphy.com/media/qanrUMM3x50mA/giphy.gif)

# Oneflow - Backend developer Assignment

Create an API using flask as presented below.

## General

All of your commits must be here, we want to see how you work.

**Register everything** including your tests/spikes, ideas if you had more time (explain how would you solve things), decisions you've made (and why), the architecture you chose. Add a `COMMENTS.md` or a `HISTORY.md` to show us your thoughts and ideas.

## The assignment
![](https://api.chucknorris.io/img/chucknorris_logo_coloured_small.png)

The applicant should design and implement a minimalistic flask API application that would let the user search, create, delete and update jokes from [Chuck Norris jokes](https://api.chucknorris.io/), that works through for example Postman. To simplify the description, we will call [Chuck Norris jokes](https://api.chucknorris.io/) as remote and application implemented in this assignment as local.

We expect the applicant to at least implement these 5 endpoints (but feel free to add more):

### `GET /jokes/?query={query}`
Free text search endpoint. You should take local and remote search results into consideration.

### `POST /api/jokes/`
Endpoint to create joke locally.

### `GET /api/jokes/{id}`
Endpoint to retrieve a joke by unique id. You should take local and remote results into consideration.

### `PUT /api/jokes/{id}`
Endpoint to update a joke by unique id. If the joke does not exist, return 404 not found. But if it does, store a updated version locally. Any subsequent reads should only see this updated version.

### `DELETE /api/jokes/{id}`
Endpoint to delete a joke by unique id. If the joke does not exist, return 404 not found. But if it does, mark the joke locally as deleted. Any subsequent reads should *NOT* see this joke.


## Technical assumptions

- You should use [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- You should consider how you would scale the API for other types of jokes and more functionality per category

## Extras

Focus on the basics and on solving the main problem, but you can also:

- Add documentation
- Add unit tests
- Add extra options/attributes to endpoints to make them more powerful

## What are we evaluating?

1. The described features and requirements.
2. Any extras you've added to your final solution.
3. Any other creative thing or feature you added by yourself.
4. In general: simplicity, clarity of your solution, architecture, documentation, code style, interface design, and the code.

## Tips

- We want you to show us how you work, break down bigger problems and prioritize them.
- It's an option to not implement everything, mock anything you think it's gonna save you time.
- It's better if you show us something small that works and is well factored rather than something complete but "buggy"
- It's better if you use open-source libraries and explain why you chose them.
- If you have any questions, please ask us :)

----
## Version 2.0
While developing the front-end, it turned out that I needed to activate CORS into flask back-end for the front-end to work. Plus, I came across a minor bug in the back-end that caused deleted jokes to be displayed in a certain scenario. I've fixed the issues and have the updated back-end and front-end. Keep in mind that the React front-end app assumes that the Flask API is running on its default port 5000. This is the default port if you're running the Flask API as instructed the README. Otherwise, I'll need to configure the Front-end app accordingly.

# Chuck Norris Joke API

This API acts as a gateway towards Chuck Norris API (api.chucknorris.io), letting the user search, create, delete and update jokes from Chuck Norris jokes, that works through Postman.

## Installation

### Conda

`conda create -n joke-api python=3.9`

`conda install -c conda-forge --file conda_requirements.txt`

### Pip

`
pip install -r pip_requirements.txt
`


## Usage

Create database file by running 'create_database.py'

`
python create_database.py
`

To start the server

`
flask run
`

Unit tests:

`
pytest
`


## API documentation
[Postman documentation](https://documenter.getpostman.com/view/1228415/TzJsed2b#bfc134f9-3b09-4a57-af10-7b905479369e)