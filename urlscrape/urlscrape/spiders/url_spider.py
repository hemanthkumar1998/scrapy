# # -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from selenium import webdriver
from time import sleep

class UrlSpiderSpider(scrapy.Spider):
    name = 'url_spider'
    url=input()
    final_url='{0}'.format(url)
    allowed_domains = ['books.toscrape.com']
    start_urls = [final_url]

    def parse(self, response):
        
        books=response.xpath('//a/@href').extract()
        # print(len(books))
        for book in books:
            abs_url=response.urljoin(book)
            yield Request(abs_url,callback=self.parse_book)
        next_url=response.xpath('//a[text()="next"]/@href').extract_first()
        abs_next_url=response.urljoin(next_url)
        yield {"url":Request(abs_next_url)}

    def parse_book(self,response):
        pass



#     #     for link in books:
#     #         yield {'links':scrapy.http.Request(url=link, callback=print_this_link)}
 
#     # def print_this_link(self, link):
#     #     print ("Link --> {this_link}".format(this_link=link))
#     #     pass
# -*- coding: utf-8 -*-

    # def parse(self, response):
    #     books = response.xpath('//h3/a/@href').extract()
    #     for book in books:
    #         absolute_url = response.urljoin(book)
    #         yield Request(absolute_url, callback=self.parse_book)

    #     # process next page
    #     next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
    #     absolute_next_page_url = response.urljoin(next_page_url)
    #     yield Request(absolute_next_page_url)

    # def parse_book(self, response):
    #     pass
