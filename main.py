from fastapi import FastAPI
from flask import jsonify
from enum import Enum
#uvicorn main:app --reload
#https://fastapi.tiangolo.com/pt/tutorial/path-params/
app = FastAPI(debug=1)

@app.get("/buscar_usuario/{id}",
        tags=['Usuário'],description='Busca somente um usuário do sistema a partir do ID informado',
        response_description="Retorna somente um usuário filtrado pelo ID em um objeto",
        status_code=200)
async def buscar_usuarios(id:str):
    name = 'Alexandre'
    cpf = '126.395.806-04'
    response = {'id': id,'name':name,'cpf':cpf}
    return response

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    
@app.get("/buscar_usuarios",
        tags=['Usuário'],description='Busca todos os usuários do sistema',
        response_description="Retorna todos usuários usuários do sistema em uma lista de objeto.",
        status_code=200)
async def buscar_usuario():
    response = {
        'has error':'false',
        'message':'Success'
        }
    return response
