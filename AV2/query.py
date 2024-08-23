class Querys:
    def __init__(self, database):
        self.db = database

    # Questão 01

    def query1a(self):
        query = "MATCH (r:Teacher {name: 'Renzo'}) RETURN r.cpf AS cpf, r.ano_nasc AS ano_nasc"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1b(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1c(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query1d(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS name, s.address AS address, s.number AS number
        """
        results = self.db.execute_query(query)
        return [result for result in results]

    # Questão 02

    def query2a(self):
        query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS ano_nasc_mais_jovem, MIN(t.ano_nasc) AS ano_nasc_mais_velho"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2b(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS media_population"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2c(self):
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS name"
        results = self.db.execute_query(query)
        return [result for result in results]

    def query2d(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS third_letter"
        results = self.db.execute_query(query)
        return [result for result in results]
