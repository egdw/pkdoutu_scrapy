# -*- coding: utf-8 -*-
import scrapy

# [
# {"title": "王者农药版《过火》，唱出你的心累 ​​​", "url": "https://www.pkdoutu.com/article/detail/9414486"},
# ]

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['pkdoutu.com']
    start_urls = ['https://pkdoutu.com/article/list/']

    def parse(self, response):
        for article in response.css("a.random_list"):
            yield{
                "title":article.css("div.random_title::text").get(),
                "url":article.css('a::attr(href)').extract_first()
            }
        next_page = response.css("#home > div > div.col-sm-9.center-wrap > div.text-center > ul > li.page-item.active > span::text").extract_first()
        hasNext = response.css("a.page-link[rel*=next]")
        if hasNext is not None:
            yield scrapy.Request(response.urljoin("?page="+str(int(next_page)+1)))
