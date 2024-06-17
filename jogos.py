from db import database

class Jogo:
    def __init__(self):
        self.db = database()

    def create(self, id, nome, desenvolvedor):
        query = "CREATE (:Jogo {id: $id, nome: $nome, desenvolvedor: $desenvolvedor})"
        self.db.run_query(query, {"id": id, "nome": nome, "desenvolvedor": desenvolvedor})

    def read(self):
        query = "MATCH (j:Jogo) RETURN j.nome AS nome"
        return self.db.run_query(query)

    def update(self, id, novo_nome, novo_desenvolvedor):
        query = "MATCH (j:Jogo {id: $id}) SET j.nome = $novo_nome, j.desenvolvedor = $novo_desenvolvedor"
        self.db.run_query(query, {"id": id, "novo_nome": novo_nome, "novo_desenvolvedor": novo_desenvolvedor})

    def delete(self, id):
        query = "MATCH (j:Jogo {id: $id}) DELETE j"
        self.db.run_query(query, {"id": id})

class Categoria:
    def __init__(self):
        self.db = database()

    def create(self, id, nome):
        query = "CREATE (:Categoria {id: $id, nome: $nome})"
        self.db.run_query(query, {"id": id, "nome": nome})

    def read(self):
        query = "MATCH (c:Categoria) RETURN c.nome AS nome"
        return self.db.run_query(query)
    
    def update(self, id, novo_nome):
        query = "MATCH (c:Categoria {id: $id}) SET c.nome = $novo_nome"
        self.db.run_query(query, {"id": id, "novo_nome": novo_nome})

    def delete(self, id):
        query = "MATCH (c:Categoria {id: $id}) DELETE c"
        self.db.run_query(query, {"id": id})