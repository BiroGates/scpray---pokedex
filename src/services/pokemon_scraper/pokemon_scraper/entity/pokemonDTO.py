
from typing import List
from .PokemonType import PokemonType;
from .PokemonEvolution import PokemonEvolution;
from .PokemonSkill import PokemonSkill;
from .PokemonEffectiveness import PokemonEffectiveness;


class PokemonDTO:
    number: int
    url: str
    name: str
    sizeInCm: int
    weight: int 
    type: List[PokemonType]
    evolutions: List[PokemonEvolution]
    skills: List[PokemonSkill]
    effectiveness: PokemonEffectiveness
    evolutionsArrow: List[str]
    skillsRaw: List[str]
