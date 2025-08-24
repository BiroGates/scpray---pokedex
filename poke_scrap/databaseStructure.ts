enum PokemonType {
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
}

type PokemonSkill = {
    url: string;
    name: string;
    desc: string;
}

type PokemonEffectiveness = {
    type: PokemonType;
    value: number; 
}

type Pokemon = {
    number: number;
    url: string;
    name: string;
    sizeInCm: number;
    weight: number; 
    type: PokemonType[];
    evolutions?: PokemonEvolution[];
    skills: PokemonSkill[];
    effectiveness: PokemonEffectiveness;
}

type PokemonEvolution = Pokemon & {
    level: string;
    item?: string;
}

