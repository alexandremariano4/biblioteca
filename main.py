from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum
#uvicorn main:app --reload
#https://fastapi.tiangolo.com/pt/tutorial/query-params-str-validations/
app = FastAPI(title='Biblioteca',
            version='1.0.0',
            description='Back-end da Biblioteca criada para estudos utilizando python na linguagem principal do back-end',swagger_ui_parameters={'deepLinking':False,'docExpansion':'list','persistAuthorization':True},)

class Sexo(str,Enum):
    M = 'M'
    F = 'F'
class Usuario(BaseModel):
    name: str  = Query(max_length=15,default='Alexandre Teste')
    cpf: str = Query(max_length=11,default='12345678901')
    sexo : Sexo = Query(default='M')
    telefone: str = Query(max_length=11,default='31973928607')
    endereço: str = Query(max_length=25,default='Rua Bão Sernado, 15')


@app.post('/usuarios/',tags=['Usuário'],summary='<Cadastra um novo usuário na base de dados>',
        description='Cadastra um único usuário no sistema',
        status_code=201)
async def cadastra_usuario(usuario: Usuario):

    usuario_dados = usuario,
    return usuario_dados


@app.get("/usuarios/{id}",
        tags=['Usuário'],description='Busca somente um usuário do sistema a partir do ID informado',summary='<Busca um usuário específico na base a partir do ID>',
        response_description="Retorna somente um usuário filtrado pelo ID em um objeto",
        status_code=200)
async def buscar_usuario(id:str):
    name = 'Alexandre'
    cpf = '126.395.806-04'
    response = {'id': id,'name':name,'cpf':cpf}
    return response



@app.get("/usuarios/",
        tags=['Usuário'],description='Busca todos os usuários do sistema',summary='<Busca todos usuários da base de dados>',
        response_description="Retorna todos usuários usuários do sistema em uma lista de objeto.",
        status_code=200)
async def buscar_usuarios():
    response = {
        'has error':'false',
        'message':'Success'
        }
    return response



class Categoria(str, Enum):
    Drama    = "Drama"
    Romance  = "Romance"
    Biografia = "Biografia"

@app.get("/categoria/{categoria}",status_code=200,tags=['Livros'],description='Busca os livros existentes na base de dados pela categoria escolhida',summary='<Busca um livro específico por categoria>')
async def buscar_livro(categoria: Categoria):
    if categoria is Categoria.Biografia:
        return {'name': 'Livro Teste de Biografia','Páginas': '526'}
    if categoria.value == 'Romance':
        return {'name': 'Livro Teste de Romance','Páginas': '526'}
    if categoria.value == 'Drama':
        return {'name': 'Livro Teste de Drama','Páginas': '526'}
    return 'Nenhum valor válido escolhido'
    


@app.get("/items/{item_id}",tags=['Exemplos Uteis'],summary='<Exemplo de parâmetro de rota (item_id) e exemplo de parâmetro de consulta (q)>')
async def read_item(item_id: str, q: str or None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
