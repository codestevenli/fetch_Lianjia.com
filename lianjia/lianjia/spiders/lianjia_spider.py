import scrapy
from lianjia.items import lianjiaItem

class lianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ["lianjia.com"]
   
    start_urls = []
    for i in range(100):
        start_urls.append("http://gz.lianjia.com/zufang/yuexiu/pg%s" % str(i+1))

    def parse(self, response):
        for sel in response.xpath("//div[@class='info-panel']"):
            lianjia = lianjiaItem()
            lianjia['name_of_community'] = sel.xpath("h2/a/text()").extract()
            lianjia['layout_of_house'] = sel.xpath("div[1]/div[1]/span[2]/text()").extract()
            lianjia['price_of_house'] = sel.xpath("div[2]/div[1]/span/text()").extract()
            lianjia['area_of_house'] = sel.xpath("div[1]/div[1]/a/span/text()").extract()
            
            lianjia['time_of_construction'] = sel.xpath("div[1]/div[1]/span[1]/span/text()").extract()  
            
            yield lianjia


"""
            #patching shanghai's issue used xpath is different  response.xpath("//div[@class='info-panel']")
            lianjia['name_of_community'] = sel.xpath("h2/a/text()").extract()
            lianjia['layout_of_house'] = sel.xpath("div[2]/div[2]/text()").extract()
            lianjia['price_of_house'] = sel.xpath("div[2]/div[1]/span/text()").extract()
            lianjia['area_of_house'] = sel.xpath("div[1]/div[1]/a/span/text()").extract()
            lianjia['floor_of_house'] = sel.xpath("div[1]/div[2]/div[1]/a[2]/text()").extract()
            lianjia['time_of_construction'] = sel.xpath("div[1]/div[1]/span[2]/text()").extract() 

            #patching normal ershoufang e.g guangzhou is this response.xpath("//div[@class='info clear']")
			lianjia['name_of_community'] = sel.xpath("div[1]/a/text()").extract()
            lianjia['layout_of_house'] = sel.xpath("div[6]/div[2]/span/text()").extract()
            lianjia['price_of_house'] = sel.xpath("div[6]/div[1]/span/text()").extract()
            lianjia['area_of_house'] = sel.xpath("div[2]/div/text()").extract()
            lianjia['time_of_construction'] = sel.xpath("div[3]/div/text()").extract() 

            #patching normal zufang is this response.xpath("//div[@class='info-panel']")
			lianjia['name_of_community'] = sel.xpath("h2/a/text()").extract()
            lianjia['layout_of_house'] = sel.xpath("div[1]/div[1]/span[2]/text()").extract()
            lianjia['price_of_house'] = sel.xpath("div[2]/div[1]/span/text()").extract()
            lianjia['area_of_house'] = sel.xpath("div[1]/div[1]/a/span/text()").extract()
            lianjia['time_of_construction'] = sel.xpath("div[1]/div[1]/span[1]/span/text()").extract()  
"""