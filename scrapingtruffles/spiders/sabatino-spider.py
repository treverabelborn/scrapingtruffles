import scrapy
from scrapingtruffles.items import TruffleProduct


class SabatinoSpider(scrapy.Spider):
    name = "sabatino"

    def start_requests(self):
        urls = [
            "https://sabatino1911.com/collections/shop-all?page=1",
            "https://sabatino1911.com/collections/shop-all?page=2",
            "https://sabatino1911.com/collections/shop-all?page=3",
            "https://sabatino1911.com/collections/shop-all?page=4",
            "https://sabatino1911.com/collections/shop-all?page=5",
            "https://sabatino1911.com/collections/shop-all?page=6",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        product_cards = response.xpath('''
            //div[contains(@class, "product-card")]
            /div[not(contains(@class, "opacity-0"))]
            /a[@class="product-card__info block w-full mb-4"]
        ''')

        for p in product_cards:
            yield TruffleProduct(
                description=p.xpath('p/text()').get(),
                price=p.xpath('div/span/text()').get())