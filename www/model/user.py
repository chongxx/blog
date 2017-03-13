# -*- coding: utf-8 -*-

__author__ = 'Dash'

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):

	__tablename__ = "user"

	id = Column(Integer, primary_key = True)
	username = Column(String)
	pwd = Column(String)
	nickname = Column(String)
	avatar = Column(String)
	state = Column(Integer)
	register_time = Column(Integer)
	email = Column(String)

# connect database
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/blog')
db_session = sessionmaker(bind = engine)

user_session = db_session()
# create new object
new_user = User(id = 2, username = 'testadmin', pwd = 'testpwd', nickname = 'testname', avatar= "https://assets-cdn.github.com/images/modules/logos_page/Octocat.png", state = 1, register_time = 1, email = "test@test.com")

user_session.add(new_user)
user_session.commit()
user_session.close()
