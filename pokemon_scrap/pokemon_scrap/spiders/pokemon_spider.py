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
    baseUrl = "https://pokemondb.net/pokedex/"

    def parse(self, response: Response):
        pokemonNames = response.css("a.ent-name::text").getall()
        i = 0;

        for name in pokemonNames:
            if i > 10:
                break;
            i+=1;
            next_page = f"https://pokemondb.net/pokedex/{name.lower()}"

            yield response.follow(
                next_page,
                callback=self.getInitialPokemonInfo,
                meta={"logger": self.logger},
                dont_filter=True
            )

    def getInitialPokemonInfo(self, response: Response):
        logger = response.meta["logger"]
        service = PokemonService(response, logger, Pokemon())

        pokemon = service.handle()
        yield {
            "name": pokemon.name,
        };


class PokemonService:
    baseUrl = "https://pokemondb.net/pokedex/"

    def __init__(self, response: Response, logger, pokemon: Pokemon):
        self.response = response
        self.logger = logger
        self.pokemon = pokemon

    def handle(self) -> Pokemon:
        self.pokemon.number = self._getNumber(self.response)
        self.pokemon.name = self._getName(self.response)
        self.pokemon.url = self.baseUrl + self.pokemon.name
        self.pokemon.sizeInCm = self._getSizeInCm(self.response)
        self.pokemon.weight = self._getWeight(self.response)
        self.pokemon.type = self._getType(self.response)
        self.pokemon.evolutionsNames = self.getEvolutions(self.response)

        return self.pokemon

    def _getName(self, response):
        name = response.css("main h1::text").get()
        self.logger.info(f"NAME: {name}")
        return name

    def _getNumber(self, response):
        number = response.css("strong::text").get()
        self.logger.info(f"NUMBER: {number}")
        return number

    def _getSizeInCm(self, response):
        size = response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedSize = round(float(re.sub(r'\s[a-z]', '', size.split(' ')[0])) * 100, 2)
        self.logger.info(f"SIZE: {treatedSize:.2f}")
        return treatedSize

    def _getWeight(self, response):
        weight = response.css("table.vitals-table tr:contains('Weight') td::text").get()
        treatedWeight = re.sub(r'\s[a-z]', '', weight.split(' ')[0])
        self.logger.info(f"WEIGHT: {treatedWeight}")
        return treatedWeight

    def _getType(self, response):
        type_ = response.css("table.vitals-table td a.type-icon::text").getall()
        self.logger.info(f"TYPE: {type_}")
        return type_

    def getEvolutions(self, response):
        evolutionNames = response.css("span.infocard-lg-data a.ent-name::text").getall()
        payload = [];

        cards = response.css('div.infocard').getall();

        for card in
        self.logger.info(f"CARDS: {cards}");

        
        return payload
