import  scrapy
#from ..items import ZlSpiderItem

class ZL_Spider(scrapy.Spider):
    name = 'ZL'
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=079&in=160400&jl=%E5%8C%97%E4%BA%AC&kw=python&p=1&isadv=0']
    def parse(self, response):
        companyName = response.xpath('//td/a[@target="_blank"]/text()')
        print(companyName.extract())
        companyAddress = response.css('[class="gzdd"]::text')
        companyAddress.pop(0)
        print(companyAddress.extract())
        Len1 = len(companyName)
        Len2 = len(companyAddress)
        print(Len1,Len2)



