import mysql.connector
from  mysql.connector.errors import IntegrityError
from messages.has_error import mensagem
from configparser import ConfigParser
config = ConfigParser()
config.read('database.ini')


def cadastrar(dados_usuario):
    conexao = mysql.connector.connect(
        host=config.get('database','host'),
        username=config.get('database','username'),
        password=config.get('database','password')
    )
    cursor = conexao.cursor()
    cursor.execute('use library;')
    try:
        if str(dados_usuario.cpf).isnumeric() == True & str(dados_usuario.telefone).isnumeric() == True :
            resultado = cursor.execute(f'''
                        INSERT INTO usuarios (nome,cpf,sexo,telefone,endereco) 
                        VALUES ('{dados_usuario.nome}','{dados_usuario.cpf}','{dados_usuario.sexo}','{dados_usuario.telefone}','{dados_usuario.endereco}');
                        ''')
        else:
            raise TypeError
        

    except IntegrityError as error:
        retorno = mensagem(1,'CPF já existente na base de dados!')
        retorno.update({'cpf':dados_usuario.cpf})   
        cursor.close()
        conexao.close()
        return retorno
    except TypeError as error:
        retorno = mensagem(1,'Valores inválidos, campo de CPF e TELEFONE devem ser numéricos!')
        retorno.update({'telefone':dados_usuario.telefone,'cpf':dados_usuario.cpf})   
        cursor.close()
        conexao.close()
        return retorno
    else:
        retorno = mensagem(0,'Usuário cadastrado na base de dados com sucesso!')
        retorno.update({'cpf':dados_usuario.cpf})
        conexao.commit()    
        cursor.close()
        conexao.close()
        return retorno
    

    