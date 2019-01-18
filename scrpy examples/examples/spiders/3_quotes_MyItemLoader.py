# -*- coding: utf-8 -*-
"""
getting multiple items from
a page using ItemLoader
"""
import scrapy
from items import Quote
from scrapy.loader import ItemLoader
from itemloaders import QuoteLoader


class QuotesSpider(scrapy.Spider):
    name = 'quotes3'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        for q in response.xpath("//div[@class='quote']"):
            l = QuoteLoader(selector=q)
            l.add_xpath('author_name', './/small[@class="author"]/text()')
            l.add_xpath('text', './/span[@class="text"]/text()')
            l.add_xpath('tags', './/a[@class="tag"]/text()')
            yield l.load_item()
