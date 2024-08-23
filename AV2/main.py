# main.py
from database import Database
from query import Querys
from teacher_crud import TeacherCRUD

def main():
    db = Database("bolt://3.239.29.216:7687", "neo4j", "rifles-executives-televisions")
    queries = Querys(db)
    teacher_crud = TeacherCRUD(db)

    # Executando as queries da Questão 01
    print("Questão 01.1:", queries.query1a())
    print("Questão 01.2:", queries.query1b())
    print("Questão 01.3:", queries.query1c())
    print("Questão 01.4:", queries.query1d())

    # Executando as queries da Questão 02
    print("Questão 02.1:", queries.query2a())
    print("Questão 02.2:", queries.query2b())
    print("Questão 02.3:", queries.query2c())
    print("Questão 02.4:", queries.query2d())

    # Executando operações CRUD na entidade Teacher
    print("\n--- CRUD Operations ---")
    print("Creating Teacher 'Chris Lima'")
    teacher_crud.create('Chris Lima', 1956, '189.052.396-66')

    print("Reading Teacher 'Chris Lima'")
    print(teacher_crud.read('Chris Lima'))

    print("Updating CPF of 'Chris Lima'")
    teacher_crud.update('Chris Lima', '162.052.777-77')

    print("Reading updated Teacher 'Chris Lima'")
    print(teacher_crud.read('Chris Lima'))

    print("Deleting Teacher 'Chris Lima'")
    teacher_crud.delete('Chris Lima')

    print("Attempting to read deleted Teacher 'Chris Lima'")
    print(teacher_crud.read('Chris Lima'))

    db.close()

if __name__ == "__main__":
    main()
