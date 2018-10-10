# -*- coding: utf-8 -*-
import scrapy
from practice.items import PracticeItem


class AkaSpider(scrapy.Spider):
    name = 'aka'
#    allowed_domains = ['https://www.w3schools.com/pHP/default.asp']
    start_urls = ['https://www.w3schools.com/pHP/php_intro.asp']

    def parse(self, response):
		item=PracticeItem()
		item['defi']=response.xpath('//div/text()').extract()[-8]
		item['sign']=response.xpath('//div/text()').extract()[-10]
		print item
		print item['defi']
		print item['sign']
#		print response.body
        
