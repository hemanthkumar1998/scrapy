# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        books=response.xpath('//*a/@href').extract()
        for link in books:
            yield {'links':scrapy.http.Request(url=link, callback=print_this_link)}
 
    def print_this_link(self, link):
        print ("Link --> {this_link}".format(this_link=link))

    #     csrf_token=response.xpath()
    #     yield FormRequtest('http://quotes.toscrape.com/login',formdata={'csrf_token':csrf_token},'name':'myself','password':'myself',
    #     callback=se;f.parse_after_login)
    # def parse_after_login(self,response):
    #     pass