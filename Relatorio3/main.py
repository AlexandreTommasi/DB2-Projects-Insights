from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex  
db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db)  

pikachu = pokedex.getPokemonByName("Pikachu")  
writeAJson(pikachu, "pikachu")

tipos = ["Fighting"]
pokemons = pokedex.getPokemonsByType(tipos)  
writeAJson(pokemons, "pokemons_por_tipo")

tipos = ["Grass", "Poison"]
pokemons = pokedex.getPokemonsWithEvolutionsByTypes(tipos)
writeAJson(pokemons, "pokemons_grama_ou_veneno_com_evolucao")

pokemons = pokedex.getPokemonsWithSingleWeakness()  
writeAJson(pokemons, "pokemons_com_1_fraqueza")

pokemons = pokedex.getPokemonsFireOrWeakAgainstFire()  
writeAJson(pokemons, "pokemons_que_sao_de_fogo_ou_fracos_contra")
