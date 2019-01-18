# -*- coding: utf-8 -*-
"""
getting multiple items from
a page using ItemLoader
"""
import scrapy
from examples.items import Quote
from scrapy.loader import ItemLoader


class QuotesSpider(scrapy.Spider):
    name = 'quotes2'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for q in response.xpath("//div[@class='quote']"):
            l = ItemLoader(item=Quote() ,selector=q)
            l.add_xpath('author_name', './/small[@class="author"]/text()')
            l.add_xpath('text', './/span[@class="text"]/text()')
            l.add_xpath('tags', './/a[@class="tag"]/text()')
            yield l.load_item()
