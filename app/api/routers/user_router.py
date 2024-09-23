from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from api.schemas.user_schema import user_schema_create
from api.dependencies.database import get_db
from sqlalchemy.orm import Session
from app.api.models.user_model import Users

user_router = APIRouter()


@user_router.get('/{i}', tags=['Users']) #Tag sirve para ser claro en la documentacion
async def get_user_by_id(i:int, db: Session = Depends(get_db)):
 
    db_user: Users = db.query(Users).filter(Users.id == i).first()
    return db_user.user_name


@user_router.post('/', tags=['Users'])
async def add_user(user: user_schema_create) -> JSONResponse:

    #Cotejar si existe en la bdd

    #return JSONResponse(content='Succesfully created.', status_code=status.HTTP_200_OK)
    return f'name: {user.user_name}, y su pass: {user.password}'
