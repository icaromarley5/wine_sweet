import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


class WineSpider(scrapy.spiders.CrawlSpider):
    name = "Wine"

    start_urls = [
        "https://www.wine.com.br/browse.ep?cID=100851&exibirEsgotados=false&pn=1&listagem=horizontal&sorter=featuredProducts-desc&filters=cVINHOS"
    ]

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths="//a[contains(@class, 'Pagination-nav Link')]"
            ),
            follow=True,
        ),
        Rule(
            LinkExtractor(
                restrict_xpaths="//article/a[contains(@class, 'js-productClick')]"
            ),
            callback="parse_wine",
        ),
    )

    def parse_wine(self, response):
        if "Suave/Doce" in response.text:
            yield {"url": response.url}
