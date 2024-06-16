import scrapy


class TruffleProduct(scrapy.Item):
    description = scrapy.Field()
    price = scrapy.Field()
