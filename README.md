![image](https://forthebadge.com/images/badges/made-with-python.svg) ![image](https://forthebadge.com/images/badges/kinda-sfw.svg)
## Chuck Norris API

![image](https://media.giphy.com/media/qanrUMM3x50mA/giphy.gif)

# Tech specifications

- Python
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Documentation made with Postman
- Javascript
- HTML / CSS

----
## Version 2.0
While developing the front-end, it turned out that I needed to activate CORS into flask back-end for the front-end to work. Plus, I came across a minor bug in the back-end that caused deleted jokes to be displayed in a certain scenario. I've fixed the issues and have the updated back-end and front-end. Keep in mind that the React front-end app assumes that the Flask API is running on its default port 5000. This is the default port if you're running the Flask API as instructed the README. Otherwise, I'll need to configure the Front-end app accordingly.

## Version 1.0

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
