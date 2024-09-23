from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from api.schemas.user_schema import user_schema_create
user_router = APIRouter()


@user_router.get('/{i}', tags=['Users']) #Tag sirve para ser claro en la documentacion
async def get_user_by_id(i:int):

    # Realizar conexion con base de datos con sqlalchemy.

    return i


@user_router.post('/', tags=['Users'])
async def add_user(user: user_schema_create) -> JSONResponse:

    #Cotejar si existe en la bdd

    #return JSONResponse(content='Succesfully created.', status_code=status.HTTP_200_OK)
    return f'name: {user.user_name}, y su pass: {user.password}'
