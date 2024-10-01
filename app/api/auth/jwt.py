from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, Request, status
from api.dependencies.database import get_db
from sqlalchemy.orm import Session
from api.utils.bcrypt import check_pass
from api.models.user_model import Users
from jose import jwt, JWTError
import os
import datetime
from pydantic import BaseModel
from typing import Annotated
oauth_schema = OAuth2PasswordBearer(tokenUrl='login')

login_router = APIRouter()

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# @login_router.get('/login2', response_model=str)
# async def a():
#     return 'BOCA'


@login_router.post('/login', response_model=TokenResponse) #Retorna un JWT si es valido el user y el password.
async def login(data_form: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db))-> TokenResponse:
    print('Boca2')
    username = data_form.username
    password = data_form.password
    user: Users|None = db.query(Users).filter(Users.user_name == username).first()
    if user and check_pass(user.hashed_pass, password):       
        
        payload={'user':username,
                 'iat':datetime.utcnow(),
                 'exp':(datetime.utcnow() + datetime.timedelta(days=1)).timestamp(),
                 'scope': 'user'
                 }
        
        token_str = encode_token(payload)
        print(token_str)
        return TokenResponse(access_token=token_str, token_type='bearer')
    else:

        raise HTTPException(detail='User or password incorrect.', status_code=status.HTTP_400_BAD_REQUEST)



def encode_token(payload: dict)->str:
    token = jwt.encode(payload,os.getenv('SECRET_KEY'), os.getenv('ALGORITHM'))
    return token


def decode_token(token:str = oauth_schema)->dict:
    payload: dict = jwt.decode(token, os.getenv('SECRET_KEY'), os.getenv('ALGORITHM'))
    return payload


def validate_token(token: str = oauth_schema)->bool:

    payload:dict = decode_token(token)
    exp_date = payload.get('exp')
    if exp_date > datetime.utcnow().timestamp():
        return True
    else:
        raise HTTPException(detail='Unauthorized: Token has expired.', status_code=status.HTTP_401_UNAUTHORIZED)
        
     