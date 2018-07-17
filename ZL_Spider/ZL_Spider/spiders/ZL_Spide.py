import  scrapy
#from ..items import ZlSpiderItem

class ZL_Spider(scrapy.Spider):
    name = 'ZL'
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?in=160400%3B160000&jl=%E5%8C%97%E4%BA%AC&kw=python%E5%BC%80%E5%8F%91&p=1&isadv=0']
    def parse(self, response):
        companyName = response.xpath('//td/a[@target="_blank"]/text()')
        print(companyName.extract())
        companyAddress = response.css('[class="gzdd"]::text')
        companyAddress.pop(0)
        print(companyAddress.extract())
        salary = response.css('[class="zwyx"]::text')
        salary.pop(0)
        print(salary.extract())
        release_time = response.xpath('//td[@class="gxsj"]/span/text()')
        print(release_time.extract())
        job_requirements = response.xpath('//li[@class="newlist_deatil_last"]/text()')
        print(job_requirements.extract())