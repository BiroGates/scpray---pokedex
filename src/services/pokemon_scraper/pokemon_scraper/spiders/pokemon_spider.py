import re
from scrapy.http import Response
import scrapy

from ..entity.Pokemon import Pokemon;
from services.PokemonGetDataService import PokemonGetDataService;

class PokemonSpider(scrapy.Spider):
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
                callback=self.getPokemonInfo,
                meta={"logger": self.logger},
                dont_filter=True
            )

    def getPokemonInfo(self, response: Response):
        logger = response.meta["logger"]
        service = PokemonGetDataService(response, logger, Pokemon())

        pokemon = service.handle()
        yield {
            "name": pokemon.name,
        };