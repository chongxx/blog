from main import db, User, Post


class UserModel(object):

	def add(model):
		db.session.add(user)
		db.session.commit()
	
	# get post 1 model
	def get(id):
		Post.query.get(id)

for x in range(3,30):
	p = Post('this is title 2 test' + str(x))
	p.id = x
	p.text = """ This is article content
					hehe
			"""
	p.publish_time = 1489680396 + x
	p.user_id = 1
	db.session.add(p)
	db.session.commit()
