from httpx import get

class CadastrarUsuario:
    def __init__(self,usuario):
        self.usuario = usuario

        
    def cadastro_usuario(self,cursor):
            usuario_dados = self.usuario.dict()
            endereco = get(f'https://viacep.com.br/ws/{self.usuario.cep}/json/').json()
            usuario_dados.update({"cidade": endereco['localidade'],
            "cep": endereco['cep'],
            "rua": endereco['logradouro'],
            "bairro": endereco['bairro']})
            return usuario_dados
        