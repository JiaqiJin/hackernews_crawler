# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class HackernewsItem(scrapy.Item):
    number = scrapy.Field()
    title = scrapy.Field()
    points = scrapy.Field()
    comments = scrapy.Field()
    request_timestamp = scrapy.Field()
    applied_filter = scrapy.Field()

