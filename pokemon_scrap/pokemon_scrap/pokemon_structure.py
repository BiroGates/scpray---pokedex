
from enum import Enum
from typing import List 

class PokemonType(Enum):
    NORMAL = 'NORMAL',
    FIRE = "FIRE",
    WATER = "WATER",
    ELETRIC = "ELETRIC",
    GRASS = "GRASS",
    ICE = "ICE",
    FIGHTING = "FIGHTING",
    POISON = "POISON",
    GROUND = "GROUND",
    FLYING = "FLYING",
    PSYCHIC = "PSYCHIC",
    BUG = "BUG",
    ROCK = "ROCK",
    GHOST = "GHOST",
    DRAGON = "DRAGON",
    DARK = "DARK",
    STEEL = "STEEL",
    FAIRY = "FAIRY"

class PokemonSkill:
    url: str
    name: str
    desc: str

class PokemonEffectiveness:
    type: PokemonType
    value: int



# Has same attributes of Pokemon but with 
class PokemonEvolution():    
    number: int
    url: str
    name: str
    sizeInCm: int
    weight: int 
    type: List[PokemonType]
    skills: List[PokemonSkill]
    effectiveness: PokemonEffectiveness
    level: str
    item: str    



class Pokemon:
    number: int
    url: str
    name: str
    sizeInCm: int
    weight: int 
    type: List[PokemonType]
    evolutions: List[PokemonEvolution]
    evolutionsNames: List[str]
    skills: List[PokemonSkill]
    effectiveness: PokemonEffectiveness

