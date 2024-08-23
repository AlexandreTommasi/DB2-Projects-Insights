from corrida import Corrida


class Motorista:
    def __init__(self, nota: int):
        self.corridas = []
        self.nota = nota

    def adicionar_corrida(self, corrida: Corrida):
        if corrida not in self.corridas:
            self.corridas.append(corrida)