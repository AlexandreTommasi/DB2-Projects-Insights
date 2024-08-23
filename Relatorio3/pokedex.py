from typing import List
from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, db: Database):
        self.db = db
    
    def getPokemonByName(self, name: str):
        pokemons = self.db.collection.find({"name": name})
        writeAJson(pokemons, "pikachu")
        return pokemons

    def getPokemonsByType(self, types: List[str]):
        pokemons = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemons_by_type")
        return pokemons

    def getPokemonsWithEvolutionsByTypes(self, types: List[str]):
        pokemons = self.db.collection.find({"type": {"$in": types}, "next_evolution": {"$exists": True}})
        writeAJson(pokemons, "pokemons_grama_ou_veneno_com_evolucao")
        return pokemons

    def getPokemonsWithSingleWeakness(self):
        pokemons = self.db.collection.find({"weaknesses": {"$size": 1}})
        writeAJson(pokemons, "pokemons_com_1_fraqueza")
        return pokemons

    def getPokemonsFireOrWeakAgainstFire(self):
        pokemons = self.db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Fire"}]})
        writeAJson(pokemons, "pokemons_que_sao_de_fogo_ou_fracos_contra")
        return pokemons
