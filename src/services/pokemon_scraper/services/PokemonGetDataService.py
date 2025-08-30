import re
from scrapy.http import Response

from pokemon_scraper.entity.Pokemon import Pokemon

# scrapy crawl poke -o ../../../output/pokemon.json
class PokemonGetDataService:
    baseUrl = "https://pokemondb.net/pokedex/"

    def __init__(self, response: Response, logger, pokemon: Pokemon):
        self.response = response
        self.logger = logger
        self.pokemon = pokemon

    def handle(self) -> Pokemon:
        self.pokemon.number = self.getNumber(self.response)
        self.pokemon.name = self.getName(self.response)
        self.pokemon.url = self.baseUrl + self.pokemon.name
        self.pokemon.sizeInCm = self.getSizeInCm(self.response)
        self.pokemon.weight = self.getWeight(self.response)
        self.pokemon.type = self.getType(self.response)
        self.pokemon.evolutionsRawData = self.getEvolutions(self.response)
        self.pokemon.skills = self.getSkills(self.response);

        return self.pokemon;

    def getName(self, response):
        name = response.css("main h1::text").get()
        self.logger.info(f"NAME: {name}")
        return name

    def getNumber(self, response):
        number = response.css("strong::text").get()
        self.logger.info(f"NUMBER: {number}")
        return number

    def getSizeInCm(self, response):
        size = response.css("table.vitals-table tr:contains('Height') td::text").get()
        treatedSize = round(float(re.sub(r'\s[a-z]', '', size.split(' ')[0])) * 100, 2)
        self.logger.info(f"SIZE: {treatedSize:.2f}")
        return treatedSize

    def getWeight(self, response):
        weight = response.css("table.vitals-table tr:contains('Weight') td::text").get()
        treatedWeight = re.sub(r'\s[a-z]', '', weight.split(' ')[0])
        self.logger.info(f"WEIGHT: {treatedWeight}")
        return treatedWeight

    def getType(self, response):
        type_ = response.css("table.vitals-table td a.type-icon::text").getall()
        self.logger.info(f"TYPE: {type_}")
        return type_

    def getEvolutions(self, response):
        numbers = response.css('div.infocard small::text').getall();
        names = response.css('div.infocard a.ent-name::text').getall();
        evolutionArrowsRaw = response.css('span.infocard-arrow').getall();
        evolutionUrls = [];

        self.logger.info(f"EVOLUTION NUMBER: {numbers}");
        self.logger.info(f"EVOLUTION NAMES: {names}");
        self.logger.info(f"EVOLUTIONS ARROWS: {evolutionArrowsRaw}");
        
        for name in names:
            evolutionUrls.append(self.baseUrl + name);

        return {
            "numbers": numbers,
            "names": names,
            "evolutionArrowsRaw": evolutionArrowsRaw,
            "evolutionUrls": evolutionUrls,
        };
    
    def getSkills(self, response: Response):
        skillsName = response.css("table.vitals-table tr:contains('Abilities') td span a::text").getall();
        skillUrl = response.css("table.vitals-table tr:contains('Abilities') td span a::text")

        for c in skillsName:
            

        self.logger.info(f"SKILL NAMES: {skillsName}");
        # skillsUrls = response.css("table.vitals-table tr:contains('Abilities') td::text");
        
        # response.follow(self.baseUrl + );
        
