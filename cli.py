from jogos import Jogo, Categoria
from db import database
class CLI:
    def __init__(self):
        self.crudJogos = Jogo()
        self.crudCategorias = Categoria()
        self.db = database()

    def adicionar_jogo(self):
        id = input("ID do Jogo: ")
        nome = input("Nome do Jogo: ")
        desenvolvedor = input("Desenvolvedor do Jogo: ")
        self.crudJogos.create(id, nome, desenvolvedor)
        print("jogo criado com sucesso")

    def atualizar_jogo(self):
        id = input("ID do Jogo: ")
        novo_nome = input("Novo Nome do Jogo: ")
        novo_desenvolvedor = input("Novo Desenvolvedor do Jogo: ")
        self.crudJogos.update(id, novo_nome, novo_desenvolvedor)
        print("jogo atualizado")

    def remover_jogo(self):
        id = input("ID do Jogo: ")
        self.crudJogos.delete(id)
        print("jogo deletado")

    def listar_jogos(self):
        jogos = self.crudJogos.read()
        for j in jogos:
            print(j['nome'])

    def adicionar_categoria(self):
        id = input("ID da Categoria: ")
        nome = input("Nome da Categoria: ")
        self.crudCategorias.create(id, nome)

    def atualizar_categoria(self):
        id = input("ID da Categoria: ")
        novo_nome = input("Novo Nome da Categoria: ")
        self.crudCategorias.update(id, novo_nome)

    def remover_categoria(self):
        id = input("ID da Categoria: ")
        self.crudCategorias.delete(id)

    def listar_categorias(self):
        categorias = self.crudCategorias.read()
        for c in categorias:
            print(c["nome"])

    def associar_jogo_categoria(self):
        id_jogo = input("ID do Jogo: ")
        id_categoria = input("ID da Categoria: ")
        query = """
        MATCH (j:Jogo {id: $id_jogo}), (c:Categoria {id: $id_categoria})
        CREATE (j)-[:PERTENCE_A]->(c)
        """
        self.db.run_query(query, {"id_jogo": id_jogo, "id_categoria": id_categoria})

    def remover_associacao_jogo_categoria(self):
        id_jogo = input("ID do Jogo: ")
        id_categoria = input("ID da Categoria: ")
        query = """
        MATCH (j:Jogo {id: $id_jogo})-[r:PERTENCE_A]->(c:Categoria {id: $id_categoria})
        DELETE r
        """
        self.db.run_query(query, {"id_jogo": id_jogo, "id_categoria": id_categoria})

    def listar_associacoes(self):
        query = """
        MATCH (j:Jogo)-[r:PERTENCE_A]->(c:Categoria)
        RETURN j.nome AS jogo, c.nome AS categoria
        """
        result = self.db.run_query(query)
        for record in result:
            print(f"Jogo: {record['jogo']}, Categoria: {record['categoria']}")


