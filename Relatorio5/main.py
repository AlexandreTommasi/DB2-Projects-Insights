from database import Database
from bdJogo import BancoDeDadosJogo

db = Database("bolt://3.93.213.236:7687", "neo4j", "screw-movers-combat")
db.drop_all()

game_db = BancoDeDadosJogo(db)

game_db.criar_jogador("Alezinhu")
game_db.criar_jogador("Calvo")
game_db.criar_jogador("Bonas")

game_db.criar_partida()
game_db.criar_partida()
game_db.criar_partida()

game_db.registrar_participacao("Alezinhu", 1)
game_db.registrar_participacao("Calvo", 1)
game_db.registrar_participacao("Bonas", 1)

game_db.registrar_participacao("Alezinhu", 2)
game_db.registrar_participacao("Calvo", 2)

game_db.registrar_participacao("Alezinhu", 3)
game_db.registrar_participacao("Bonas", 3)

game_db.registrar_resultado(1, "Alezinhu venceu")
game_db.registrar_resultado(2, "Calvo venceu")
game_db.registrar_resultado(3, "Alezinhu venceu")

print("Jogadores:")
print(game_db.obter_jogadores())
print("Partidas:")
print(game_db.obter_partidas())

game_db.deletar_jogador("Calvo")
game_db.deletar_partida(2)

print("Jogadores após exclusão:")
print(game_db.obter_jogadores())
print("Partidas após exclusão:")
print(game_db.obter_partidas())

db.close()
