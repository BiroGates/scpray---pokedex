from pokemon_scrap.pokemon_structure import (
    Pokemon,
    PokemonEvolution
)

import re
from scrapy.http import Response
import scrapy


class PokeSpider(scrapy.Spider):
    name = "poke"
    start_urls = ["https://pokemondb.net/pokedex/all"]
    baseUrl = "https://pokemondb.net/pokedex/";

    def parse(self, response: Response):
        pokemonNames = response.css("a.ent-name::text").getall();

        for name in pokemonNames:
            next_page = f"https://pokemondb.net/pokedex/{name.lower()}"

            yield response.follow(
                next_page,
                callback=self.getInitialPokemonInfo,
                meta={ "log": self.log }
            )
        
    
    def getInitialPokemonInfo(self, response: Response):
        log: scrapy.Spider.log =  response.meta["log"]       
        service = PokemonService(response, log, Pokemon());
        
        pokemon = service.handle();
        log(pokemon);
        for evolution in pokemon.evolutionsNames:
            yield response.follow(
                self.baseUrl + evolution,
                callback=self.getEvolutions,
                meta={ "log": self.log, "pokemon": pokemon }
            )


    def getEvolutions(self, response: Response):
        log = response.meta["log"];
        pokemon = response.meta["pokemon"];
        service =  PokemonEvolutionService(response, log, pokemon);
        service.handle();
        

        


class PokemonService:
    baseUrl = "https://pokemondb.net/pokedex/";
    
    def __init__(self, response: Response, log: scrapy.Spider.log, pokemon: Pokemon):
        self.response = response
        self.log = log;
        self.pokemon = pokemon
        pass
    
    def handle(self) -> Pokemon :
        self.pokemon.number = self._getNumber(self.response);
        self.pokemon.name =  self._getName(self.response);
        self.pokemon.url =  self.baseUrl + self.pokemon.name;
        self.pokemon.sizeInCm = self._getSizeInCm(self.response);
        self.pokemon.weight =  self._getWeight(self.response);
        self.pokemon.type =  self._getType(self.response);
        self.pokemon.evolutionsNames = self.getEvolutions(self.response);
        
        return self.pokemon;

    def _getName(self, response):
        name = response.css("main h1::text").get()
        self.log(f"NAME: {name}");
        return name;

    def _getNumber(self, response):
        number = response.css("strong::text").get()
        self.log(f"NUMBER: {number}");
        
        return number
    
    def _getSizeInCm(self, response):
        size = response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedSize = round(float(re.sub(r'\s[a-z]', '', size.split(' ')[0])) * 100, 2);
        self.log(f"SIZE: {treatedSize:.2f}");
        
        return treatedSize
    
    def _getWeight(self, response):
        weight = response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedWeight = re.sub(r'\s[a-z]', '', weight.split(' ')[0])
        self.log(f"WEIGHT: {treatedWeight}");
        
        return treatedWeight;
    
    def _getType(self, response):
        type = response.css("table.vitals-table td a.type-icon::text").getall()
        self.log(f"TYPE: {type}");
        return type
    
    def getEvolutions(self, response):
        evolutionsNames = response.css("span.infocard-lg-data a.ent-name::text").getall();
        self.log(f"EVOLUTIONS: {evolutionsNames}");
        return evolutionsNames
    
    def getskills(self):
        pass
    
    def _getEffectiveness(self):
        pass




class PokemonEvolutionService(PokemonService):
    def __init__(self, response: Response, log: scrapy.Spider.log, pokemon: Pokemon):
        self.response = response
        self.log = log
        self.pokemon = pokemon
        
    
    def handle(self):
        self.log(f"INSIDE OF EVOLUTIONS OF: {self.pokemon.name}")
        #super()._getName();
        #super()._getNumber();
        return;

    def _getItems():
        pass;

    def _getLevel():
        pass;