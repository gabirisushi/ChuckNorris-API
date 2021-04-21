from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Joke(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  remote_id = db.Column(db.String(80), unique=True, nullable=True)
  text = db.Column(db.Text, unique=False, nullable=False)
  deleted = db.Column(db.Boolean, unique=False, nullable=False, default=False)

  def __repr__(self):
      return '<Joke %r>' % self.text

  def uid(self):
    if self.remote_id is not None:
      return self.remote_id
    else:
      return 'local' + str(self.id)