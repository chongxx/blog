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
	pws = Column(String)
	nickname = Column(String)
	avatar = Column(String)
	register_time = Column(String)
	email = Column(String)

# connect database
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/blog')
db_session = sessionmaker(bind = engine)

user_session = db_seesion()
# create new object
new_user = User(id = 1, username = 'testadmin', pwd = 'testpwd', nickname = 'testname', avatar= "https://assets-cdn.github.com/images/modules/logos_page/Octocat.png", state = 1, register_tiem = 1, email = "test@test.com")

user_session.add(new_user)
user_session.commit()
session.colse()
