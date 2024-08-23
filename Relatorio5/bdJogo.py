class BancoDeDadosJogo:
    def __init__(self, database):
        self.db = database

    def criar_jogador(self, nome):
        query = "CREATE (:Player {nome: $nome})"
        parametros = {"nome": nome}
        self.db.execute_query(query, parametros)

    def criar_partida(self):
        query = "CREATE (:Match)"
        self.db.execute_query(query)

    def registrar_participacao(self, jogador_nome, partida_id):
        query = "MATCH (p:Player {nome: $jogador_nome}) MATCH (m:Match) WHERE ID(m) = $partida_id CREATE (p)-[:PARTICIPA]->(m)"
        parametros = {"jogador_nome": jogador_nome, "partida_id": partida_id}
        self.db.execute_query(query, parametros)

    def registrar_resultado(self, partida_id, resultado):
        query = "MATCH (m:Match) WHERE ID(m) = $partida_id SET m.resultado = $resultado"
        parametros = {"partida_id": partida_id, "resultado": resultado}
        self.db.execute_query(query, parametros)

    def obter_jogadores(self):
        query = "MATCH (p:Player) RETURN p.nome AS nome"
        resultados = self.db.execute_query(query)
        return [resultado["nome"] for resultado in resultados]

    def obter_partidas(self):
        query = "MATCH (m:Match) RETURN ID(m) AS id, m.resultado AS resultado"
        resultados = self.db.execute_query(query)
        return [{"id": resultado["id"], "resultado": resultado["resultado"]} for resultado in resultados]

    def deletar_jogador(self, nome):
        query = "MATCH (p:Player {nome: $nome}) DETACH DELETE p"
        parametros = {"nome": nome}
        self.db.execute_query(query, parametros)

    def deletar_partida(self, partida_id):
        query = "MATCH (m:Match) WHERE ID(m) = $partida_id DETACH DELETE m"
        parametros = {"partida_id": partida_id}
        self.db.execute_query(query, parametros)
