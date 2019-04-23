import scrapy
from scrapy.crawler import CrawlerProcess
class LizaDno(scrapy.Spider):
    name = "dnichaviy kod"


def regions(self):
    urls = ["https://lizaalert.org/forum/viewforum.php?f=179"] #Центральный регион
    for url in urls:
        yield scrapy.Request( url=url, callback=self.oblast)


def oblast(self,response):
    oblast = response.css('dl.icon > dt > a::attr(href)').extract()
    new_oblast = list()
    for i in oblast:
        m = i.replace("./", "https://lizaalert.org/forum/")
        new_oblast.append(m)
    oblast_css = new_oblast # Все url областей в центральном регионе
    for url in oblast_css:
        yield response.follow( url=url, callback=self.man)


def man(self, response):
    man = sel.css('dl.icon > dt > a::attr(href)').extract()
    new_man=list()
    for i in man:
        m = i.replace("./", "https://lizaalert.org/forum/")
        new_man.append(m)
    man_css = new_man # все url людей
    for url in man_css:
        yield response.follow( url=url, callback=self.parse)


def parse(self, response):
    man_descr = response.css('div.content').xpath('./span[@style="font-size: 140%; line-height: 116%;"]/span[@style="font-weight: bold"]').extract()
    yield man_descr
