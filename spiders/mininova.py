# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import DoubanmovieItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from tutorial.oo import list_first_item ,strip_null,deduplication ,clean_link,clean_url
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class MovieSpider(CrawlSpider):
    name = "doubanmovie"
    start_urls = (
            'http://www.7160.com/',
    )

    #rules = [Rule(SgmlLinkExtractor(allow=(r'http://www.7160.com/meinv/\d+.*' ,)),callback="parse_item")]
   
    def parse(self,response):
        sel=Selector(response)
        base_url = get_base_url(response)
        item=DoubanmovieItem()
        item[ 'title']=sel.xpath('//div[@class="main"]/h3/text()').extract()
        #item['content']=sel.xpath('//*[@id="contentText"]/div[1]/text()').extract()
        relative_url=sel.xpath( '//div[@class="img"]/a/img/@src' ).extract()
        item[ 'image_urls']=[urljoin_rfc(base_url, ru) for ru in relative_url]
        yield item
        
        next_link=list_first_item(sel.xpath(u'//div[@class="page"]/a[text()="下一页"]/@href').extract())
        if next_link:
            next_link = clean_url(response.url, next_link, response.encoding)
            yield Request(url=next_link,callback= self.parse)
           
        for detail_link in sel.xpath(u'//a[contains(@href,"meinv")]/@href' ).extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link)


    