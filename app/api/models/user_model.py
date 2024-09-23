from sqlalchemy import Column, Integer, String, BINARY
from dependencies.database import base

class Users(base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True, unique=True)
    hashed_pass = Column(BINARY)
    salt = Column(BINARY)


    