from sqlalchemy import Column, Integer, String, VARBINARY
from api.dependencies.database import base

class Users(base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String, index=True, unique=True)
    hashed_pass = Column(VARBINARY)
    
    def __init__ (self, user_name, hashed_pass):
        
        self.user_name = user_name
        self.hashed_pass = hashed_pass

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
        }


    