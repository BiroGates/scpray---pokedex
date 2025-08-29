
from typing import List
from .PokemonType import PokemonType;
from .PokemonSkill import PokemonSkill;
from .PokemonEffectiveness import PokemonEffectiveness;


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

