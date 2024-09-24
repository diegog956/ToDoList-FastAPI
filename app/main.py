from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn
from api.routers.user_router import user_router

app = FastAPI(title='ToDoList')

@app.get('/')
def home():
    return JSONResponse(content='Welcome', status_code=status.HTTP_200_OK)

app.include_router(prefix='/API/users',router=user_router)

if __name__ == '__main__':

    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True)
