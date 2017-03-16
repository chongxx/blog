class Config(object):
	pass

class ProdConfig(Config):
	pass

class DevConfig(Config):
	DEBUG= True
	# config database uri
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost:3306/blog'
	# show sqlalchemy operate database log
	SQLALCHEMY_ECHO = True
