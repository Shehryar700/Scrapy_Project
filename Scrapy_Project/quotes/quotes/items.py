# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    pass

class AboutItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    pass

class CombinedItem(scrapy.Item):
    quote = scrapy.Field()
    tags = scrapy.Field()
    birthdate = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
