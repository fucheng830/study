# -*- coding: utf-8 -*-
'''
Created on 2015年3月30日

@author: Administrator
'''
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MyImagesPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
            

    
    def item_completed(self, results, item, info):
        #print results
        
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            item['error_image'] = results.url
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
