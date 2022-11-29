import mysql.connector
from  mysql.connector.errors import IntegrityError
from messages.has_error import mensagem



def cadastrar(dados_usuario):
    conexao = mysql.connector.connect(
        host='localhost',
        username='root',
        password='123456'
    )
    cursor = conexao.cursor()
    cursor.execute('use library;')
    try:
        resultado = cursor.execute(f'''
                    INSERT INTO usuarios (nome,cpf,sexo,telefone,endereco) 
                    VALUES ('{dados_usuario.nome}','{dados_usuario.cpf}','{dados_usuario.sexo}','{dados_usuario.telefone}','{dados_usuario.endereco}');
                    ''')

    except IntegrityError as error:
        retorno = mensagem(1,'CPF já existente na base de dados!')
        retorno.update({'cpf':dados_usuario.cpf})   
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
    

    