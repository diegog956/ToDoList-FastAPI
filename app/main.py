from fastapi import FastAPI, status, Request, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from api.routers.user_router import user_router
from api.auth.jwt import login_router, validate_token


app = FastAPI(title='ToDoList')

#@app.add_middleware() Para cuando lo coloque en otra carpeta, se importa y se agrega.

#Los middleware son para todas o casi todas las rutas. (Ver Loggin o CORS)

@app.middleware('http')
async def defino_middle(request: Request, call_next):
    print(f"Method: {request.method}\n")
    print(f"URL: {request.url}\n")
    print(f"Query Params: {request.query_params}\n")
    print(f"Headers: {request.headers}\n")
    print(f"Client: {request.client}\n")
    response = await call_next(request)
    return response 

@app.get('/')
def home():
    return JSONResponse(content='Welcome', status_code=status.HTTP_200_OK)

app.include_router(prefix='/API/users',router=user_router)
app.include_router(router=login_router)

# if __name__ == '__main__':
    
    #uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)