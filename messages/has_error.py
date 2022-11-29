def mensagem(code,msg):
    msg_code = {
        0 : {
            'has_error': False,
            'message': msg
            },
        1 : {
            'has_error': True,
            'message': msg
            }
    }
    return msg_code[code]

