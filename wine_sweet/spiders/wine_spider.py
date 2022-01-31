import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

"""

class WineSpider(scrapy.Spider):
    name = "Wine"

    url_base = "https://www.wine.com.br"
    url_base_navigation = (
        url_base
        + "/browse.ep?cID=100851&exibirEsgotados=false&pn={page}&listagem=horizontal&sorter=featuredProducts-desc&filters=cVINHOS"
    )
    start_urls = [url_base_navigation.format(page=1)]
    last_page = None

    def parse(self, response):
        if not self.last_page:
            self.last_page = int(
                response.xpath(
                    '//div[contains(@class, "Pagination")]/ul/li[last()]/a/text()'
                ).get()
            )
            response.css("div.Pagination").get()

        links = [
            self.url_base + link
            for link in response.xpath(
                "//a[contains(@class, 'js-productClick')]/@href"
            ).getall()
        ]
        yield {"links": links}

        page_links = [
            self.url_base_navigation.format(page=page)
            for page in range(2, self.last_page + 1)
        ]
        for link in page_links:
            yield scrapy.Request(link, callback=self.parse)
        """


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
