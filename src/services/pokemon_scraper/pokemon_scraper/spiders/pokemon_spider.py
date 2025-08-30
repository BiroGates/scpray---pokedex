from scrapy.http import Response
import scrapy

from ..entity.Pokemon import Pokemon;
from services.PokemonGetDataService import PokemonGetDataService;

class PokemonSpider(scrapy.Spider):
    name = "poke"
    start_urls = ["https://pokemondb.net/pokedex/all"]
    baseUrl = "https://pokemondb.net/pokedex/"
    limit = 10;

    def parse(self, response: Response):
        pokemonNames = response.css("a.ent-name::text").getall()
        
        i = 0;
        for name in pokemonNames:
            i+=1;
            if i > self.limit:
                break;
            yield response.follow(
                self.baseUrl + name,
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

    def getPokemonSkills(self, response: Response):
        logger = response.meta["logger"];
        pokemon = response.meta["pokemon"];
        service = PokemonGetDataService(response, logger, Pokemon())

        pokemon = service.handle()