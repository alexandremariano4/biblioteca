class Book:   
    @staticmethod
    def cadastrar_livro(db,livro):
        cursor = db.cursor()
        cursor.execute('use biblioteca;')
        cursor.execute(f'''
                        INSERT INTO biblioteca.livro(
                        livro.nome_livro,
                        livro.nome_autor,
                        livro.nome_editora,
                        livro.qtd_paginas,
                        livro.qtd_estoque)
                        VALUES(
                        '{livro['nome_livro']}',
                        '{livro['nome_autor']}',
                        '{livro['nome_editora']}',
                        {livro['qtd_paginas']},
                        {livro['qtd_estoque']});
                        ''')
        db.commit()
        return True
    
    @staticmethod
    def apagar_livro(db,id_livro):
        cursor = db.cursor()
        cursor.execute('use biblioteca;')
        cursor.execute(f'''DELETE FROM livro WHERE id={id_livro};''')
        db.commit()