from httpx import get 


class AlterarUsuario:
    def __init__(self,usuario):
        self.usuario = usuario
    
    def alterar_usuario(self):
        endereco = get(f'https://viacep.com.br/ws/{self.usuario.cep}/json/').json()
        usuario_atual = {
        "id": '1',
        "nome": "Alexandre Teste",
        "cpf": "12345678901",
        "sexo": "M",
        "telefone": "31973928607",
        "cidade": endereco['localidade'],
        "cep": endereco['cep'],
        "rua": endereco['logradouro'],
        "bairro": endereco['bairro'],
        }
        usuario_atual.update({'name':'Nome Alterado'})
        return usuario_atual