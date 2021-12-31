# -*- coding: utf-8 -*-
import scrapy


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['pkdoutu.com/so']
    start_urls = ['http://pkdoutu.com/so/']

    def parse(self, response):
        pass
    