from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from api.schemas.user_schema import UserSchemaCreate, UserResponse
from api.dependencies.database import get_db
from sqlalchemy.orm import Session
from api.models.user_model import Users
from typing import List
import bcrypt

user_router = APIRouter()

@user_router.get('/{i}', tags=['Users']) #Tag sirve para ser claro en la documentacion
async def get_user_by_id(i:int, db: Session = Depends(get_db)) -> str:
    return 'OK'
    # db_user: Users | None = db.query(Users).filter(Users.user_id == i).first()
    # if db_user is not None:
    #     return db_user.user_name
    # else:
    #     raise HTTPException(detail='User not found in database.', status_code=status.HTTP_404_NOT_FOUND)

@user_router.get('/', tags=['Users'], response_model=List[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(Users).all()
    if users:
        return users
    else:
        raise HTTPException(detail='No users registered in database', status_code=status.HTTP_404_NOT_FOUND)


@user_router.post('/', tags=['Users'])
async def add_user(user: UserSchemaCreate, db: Session = Depends(get_db)) -> JSONResponse:

    user_db = db.query(Users).filter(Users.user_name == user.user_name).first()
    
    print(user)

    if user_db is None:

        hashed_pass = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        new_user = Users(user.user_name, hashed_pass)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return JSONResponse(content=new_user.to_dict(), status_code=status.HTTP_200_OK)

    else:
        raise HTTPException(detail="User already exists.", status_code=status.HTTP_409_CONFLICT)


 
