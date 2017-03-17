from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def home():
	return '<h1>Hello</h1>'

if __name__ == '__main__':
	app.run()


# create a model
class User(db.Model):

	__tablename__ = 'user'

	id = db.Column(db.Integer(), primary_key = True)
	username = db.Column(db.String(255))
	pwd = db.Column(db.String(255))
	avatar = db.Column(db.String(255))
	register_time = db.Column(db.Integer())
	state = db.Column(db.Integer())
	nickname = db.Column(db.String(16))

	posts = db.relationship(
		'Post',
		backref='user',
		lazy='dynamic'
	)
	def __init__(self, username):
		self.username = username

	def __repr__(self):
		return "User '{}'".format(self.username)


class Post(db.Model):

	__tablename__ = 'post'

	id = db.Column(db.Integer(), primary_key = True)
	title = db.Column(db.String(225))
	text = db.Column(db.Text())
	show_count = db.Column(db.Integer())
	publish_time = db.Column(db.DateTime)
	user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __init__(self, title):
		self.title = title

	def __repr__(self):
		return "<Post  '{}'>".format(self.title)
