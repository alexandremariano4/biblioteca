from mysql.connector import connect 
from configparser import ConfigParser
from book.book import Book
from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response , Request
from pydantic import BaseModel


server = Flask(__name__)
spec = FlaskPydanticSpec('flask',title='Biblioteca')
spec.register(app=server)


config = ConfigParser()
config.read('settings.ini')
db_params = dict(config['database'])
db = connect(
    host=db_params['host'],
    username=db_params['username'],
    password=db_params['password']
)


class Livro(BaseModel):
    nome_livro: str
    nome_autor: str
    nome_editora: str
    qtd_paginas: str
    qtd_estoque: str

class ApagarLivro(BaseModel):
    id:int
    



@server.post('/cadastro_livro')
@spec.validate(tags=['Livros'],body=Request(Livro),resp=Response('HTTP_201'))
def cadastro_livro():
    """Insere um livro no banco de dados"""
    livro = request.context.body.dict()
    Book.cadastrar_livro(db=db,livro=livro)
    return livro,201




@server.delete('/apagar_livro/<int:id>')
@spec.validate(tags=['Livros'],resp=Response('HTTP_204'))
def apagar_livro(id):
    """Apaga um livro do banco de dados"""
    Book.apagar_livro(db=db,id_livro=id)
    return f'{f"""Livro com id {id} excluído com sucesso"""}',204

if __name__ == '__main__':
    server.run(debug=1) 