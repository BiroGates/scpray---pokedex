from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from pokemon_scraper.spiders.pokemon_scalar_spider import PokemonSpider
from pokemon_scraper.spiders.pokemon_skills_spider import PokemonSkillSpider

if __name__ == "__main__":
    settings = {
        "FEEDS": {
            "src/output/skill.json": {
                "format": "json",
                "encoding": "utf8",
                "store_empty": False,
                "fields": None,
                "indent": 4, # Para o JSON ficar bem formatado
                "overwrite": True # Sobrescreve o arquivo a cada execução
            },
        }
    }
    
    project_settings = get_project_settings()
    project_settings.update(settings)
    process = CrawlerProcess(project_settings)

    
    print("Rodando PokemonSkillSpider...")
    process.crawl(PokemonSkillSpider)
    print("PokemonSkillSpider finalizado ✅")

        

    settings = {
        "FEEDS": {
            "src/output/pokemons.json": {
                "format": "json",
                "encoding": "utf8",
                "store_empty": False,
                "fields": None,
                "indent": 4, # Para o JSON ficar bem formatado
                "overwrite": True # Sobrescreve o arquivo a cada execução
            },
        }
    }
    
    project_settings.update(settings)
    process = CrawlerProcess(project_settings)

    print("Rodando PokemonSpider...")
    process.crawl(PokemonSpider)
    print("PokemonSpider finalizado ✅")
    

    process.start() 