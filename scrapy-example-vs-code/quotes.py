# -*- coding: utf-8 -*-
import json
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        token = response.css(
            'input[name="csrf_token"]::attr(value)').extract_first()
        data = {
            'csrf_token': token,
            'username': 'abc',
            'password': 'abc',
        }
        yield scrapy.FormRequest(url=self.login_url, formdata=data, callback=self.parse_quote)

    def parse_quote(self, response):
        for q in response.css('div.quote'):
            yield {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css('small.author ~ a[href*="goodreads.com"]::attr(href)').extract_first(),
            }
