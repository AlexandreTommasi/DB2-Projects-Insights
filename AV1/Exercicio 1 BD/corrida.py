class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = None

    def adicionar_passageiro(self, passageiro):
        self.passageiro = passageiro
