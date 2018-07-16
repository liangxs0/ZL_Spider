import  scrapy
#from ..items import ZlSpiderItem

class ZL_Spider(scrapy.Spider):
    name = 'ZL'
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&sm=0&p=1']
    def parse(self, response):
        for companyName in response.xpath('/html/body//a/text()'):
            print(companyName.extract())
        for jobName in response.xpath('//span/text()'):
            print(jobName)

