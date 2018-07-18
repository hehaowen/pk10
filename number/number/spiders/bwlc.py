# -*- coding: utf-8 -*-
import scrapy

from ..items import NumberItem


class BwlcSpider(scrapy.Spider):
    name = 'bwlc'
    allowed_domains = ['bwlc.net']
    start_urls = ['http://www.bwlc.net/bulletin/trax.html']

    def parse(self, response):
        rh = NumberItem()
        qishu = response.xpath('//table[@class="tb"]//tr[2]/td[1]/text()').extract()
        haoma = response.xpath('//table[@class="tb"]//tr[2]/td[2]/text()').extract()
        shijian = response.xpath('//table[@class="tb"]//tr[2]/td[3]/text()').extract()
        for i,j,z in zip(qishu,haoma,shijian):
            rh['qishu']=i
            rh['haoma']=j
            rh['shijian']=z
            yield rh
