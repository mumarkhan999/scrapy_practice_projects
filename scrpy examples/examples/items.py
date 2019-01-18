# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Quote(scrapy.Item):
    author_name = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()

