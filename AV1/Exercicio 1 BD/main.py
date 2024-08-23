from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI


db = Database(database="Exercicio1Lab", collection="Motoristas")
lab = MotoristaDAO(database=db, collection="Motoristas")

if __name__ == "__main__":
    motorista_cli = MotoristaCLI()
    motorista_cli.executar()
