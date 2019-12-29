# -*- coding: utf-8 -*-
import scrapy
import nltk
from textblob import TextBlob


class TwitterSpiderSpider(scrapy.Spider):
    a=input()
    url='https://twitter.com/'+a
    name = 'twitter_spider'
    allowed_domains = ['https://twitter.com']
    start_urls = [url]


    def parse(self, response):
        
        twitter=response.xpath('//*[@class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]/text()').extract()
        for tweets in range(5):
            print()
            blob=TextBlob(twitter[tweets])
            print(twitter[tweets])
            print()
            sentiment=format(blob.sentiment)
            print("Positive when polarity greater than 0-----negative when polarity lesser than 0")
            print(format(blob.sentiment))
            print()
            yield{"tweets":twitter[tweets],"sentiment_analysis":sentiment,"comments":"Positive when polarity greater than 0-----negative when polarity lesser than 0"}
       
