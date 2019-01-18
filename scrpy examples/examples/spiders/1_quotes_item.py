# -*- coding: utf-8 -*-
"""
getting multiple items from 
a page using itmes (Quote)
"""
import scrapy
from examples.items import Quote


class QuotesSpider(scrapy.Spider):
    name = 'quotes1'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for item in response.css("div.quote"):
            quote = Quote()
            quote["author_name"] = item.css('small.author::text').extract_first()
            quote["text"] = item.css('span.text::text').extract_first()
            quote["tags"] = item.css("a.tag::text").extract()
            yield quote
