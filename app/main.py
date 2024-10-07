from fastapi import FastAPI, status, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from api.routers.user_router import user_router
from api.auth.jwt import login_router, validate_token
import datetime

app = FastAPI(title='ToDoList')

#@app.add_middleware() Para cuando lo coloque en otra carpeta, se importa y se agrega.
#Los middleware son para todas o casi todas las rutas. (Ver Loggin o CORS)

loggin_dict:dict = {}

@app.middleware('http')
async def defino_middle(request: Request, call_next):
    
    time = datetime.datetime.now(datetime.timezone.utc)
    print(loggin_dict)
    if request.client.host in loggin_dict.keys() and loggin_dict[request.client.host] + datetime.timedelta(seconds=2) > time :
            raise HTTPException(detail='Too many request.', status_code=status.HTTP_429_TOO_MANY_REQUESTS)
    
    loggin_dict[request.client.host] = time
    
    response = await call_next(request)
    
    return response 

@app.get('/')
def home():
    return JSONResponse(content='Welcome', status_code=status.HTTP_200_OK)

app.include_router(prefix='/API/users',router=user_router)
app.include_router(router=login_router)

# if __name__ == '__main__':
    
    #uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)