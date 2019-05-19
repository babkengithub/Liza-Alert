# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class UsersSpider(scrapy.Spider):
    name = 'users'

    def start_requests(self):
        start_urls = 'https://lizaalert.org/forum/viewforum.php?f=276'
        yield scrapy.Request(url=start_urls, callback=self.parse)

    def parse(self, response):
        select = Selector(text= response.)
        message = select.xpath('//dl[@class="icon"]/dt/a/text()').extract()
        link = select.xpath('//dl[@class="icon"]/dt/a/@href').extract()
        prick_dict = dict()
        for i, j in zip(message, link):
            prick_dict[i] = j
        yield prick_dict

        next_page = select.xpath('//fieldset[@class="display-options"]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
