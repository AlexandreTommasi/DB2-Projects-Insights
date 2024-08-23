from corrida import Corrida
from motorista import Motorista
from passageiro import Passageiro


class MotoristaCLI:
    def __init__(self):
        self.motoristas = []  # Lista para armazenar os motoristas
        self.corridas = []  # Lista para armazenar as corridas
        self.passageiros = []  # Lista para armazenar os passageiros

    def menu(self):
        """
        Exibe o menu de opções.
        """
        print("=== Menu MotoristaCLI ===")
        print("1. Criar Passageiro")
        print("2. Criar Corrida")
        print("3. Criar Motorista")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        return opcao

    def criar_passageiro(self):
        """
        Cria um objeto do tipo Passageiro.
        """
        nome = input("Digite o nome do passageiro: ")
        documento = input("Digite o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        self.passageiros.append(passageiro)
        return passageiro

    def criar_corrida(self):
        """
        Cria um objeto do tipo Corrida.
        """
        nota = int(input("Digite a nota da corrida: "))
        distancia = float(input("Digite a distância da corrida (em km): "))
        valor = float(input("Digite o valor da corrida: "))
        corrida = Corrida(nota, distancia, valor)
        self.corridas.append(corrida)
        return corrida

    def criar_motorista(self):
        """
        Cria um objeto do tipo Motorista.
        """
        nota = int(input("Digite a nota do motorista: "))
        motorista = Motorista(nota)
        self.motoristas.append(motorista)
        return motorista

    def executar(self):
        while True:
            opcao = self.menu()
            if opcao == "1":
                passageiro = self.criar_passageiro()
            elif opcao == "2":
                corrida = self.criar_corrida()
            elif opcao == "3":
                motorista = self.criar_motorista()
            elif opcao == "4":
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

