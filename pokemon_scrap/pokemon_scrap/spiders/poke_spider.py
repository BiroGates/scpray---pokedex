from pathlib import Path

from pokemon_scrap.pokemon_structure import (
    Pokemon
)

import re
from scrapy.http import Response
import scrapy


class PokeSpider(scrapy.Spider):
    name = "poke"
    start_urls = ["https://pokemondb.net/pokedex/all"]

    def parse(self, response: Response):
        pokemonNames = response.css("a.ent-name::text").getall();

        i = 0
        maxCount = 10;

        for name in pokemonNames:
            if i > maxCount:
                break;
            i += 1

            next_page = f"https://pokemondb.net/pokedex/{name.lower()}"
            newPokemon = Pokemon();
            newPokemon.name = name;
            newPokemon.url = next_page;
            

            yield response.follow(
                next_page,
                callback=self.getFullAtributes,
                meta={"pokemon": newPokemon, "log": self.log }
            )
        
    
    def getFullAtributes(self, response: Response):
        pokemon: Pokemon = response.meta["pokemon"]
        log: scrapy.Spider.log =  response.meta["log"]
        
        service = PokeService(response, pokemon, log);
        service.start();

        yield {
            "name": pokemon.name,
            "url": pokemon.url,
            "number": pokemon.number,
            "sizeInCm": pokemon.sizeInCm,
            "weigthInKg": pokemon.weight,
            "type": pokemon.type,
        }
        


class PokeService:
    response: Response;
    def __init__(self, response: Response, pokemon: Pokemon, log: scrapy.Spider.log):
        self.response = response
        self.pokemon = pokemon
        self.log = log;
        pass
    
    def start(self, getEvolutions):
        if(getEvolutions):
            self.getEvolutions()

        self.getNumber()
        self.getSizeInCm()
        self.getWeight()
        self.getType()
        # self.getskills()
        # self.getEffectiveness()
        return

    def getNumber(self):
        number = self.response.css("strong::text").get()
        self.log(f"NUMBER: {number}");
        
        return number
    
    def getSizeInCm(self):
        size = self.response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedSize = round(float(re.sub(r'\s[a-z]', '', size.split(' ')[0])) * 100, 2);
        self.log(f"SIZE: {treatedSize:.2f}");
        
        return treatedSize
    
    def getWeight(self):
        weight = self.response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedWeight = re.sub(r'\s[a-z]', '', weight.split(' ')[0])
        self.log(f"WEIGHT: {treatedWeight}");
        
        return treatedWeight;
    
    def getType(self):
        type = self.response.css("table.vitals-table td a.type-icon::text").getall()
        self.log(f"TYPE: {type}");
        return type
    
    def getEvolutions(self):
        evolutions = self.response.css("span.infocard-lg-data a.ent-name::text").getall();
        self.log(f"{evolutions} ===============");
        return
    
    def getskills(self):
        pass
    
    def getEffectiveness(self):
        pass




