# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import log
from twisted.enterprise import adbapi
from scrapy.http import Request

import MySQLdb
import MySQLdb.cursors
from oss.oss_api import *
import re


class DoubanmoivePipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'python',
                user = 'root',
                passwd = '',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item
    
   
    def _conditional_insert(self,tx,item):
        tx.execute("select * from pic where title= %s",(item['title'][0],))
        result=tx.fetchone()
        log.msg(result,level=log.DEBUG)
        print result
        if result:
            log.msg("Item already stored in db:%s" % item,level=log.DEBUG)
        else:
             
            up_load="images/"+item['image_paths'][0]#本地上传路径
            img=re.match(r'^full/(\w+.*)$',item['image_paths'][0])
            img_name=img.group(1)#图片名称
            oss=OssAPI("oss-cn-beijing.aliyuncs.com", "7cqkGNjffwSTGrN5", "uCQT0NL2h0oGbnumwCsxqeLK04y4RZ")#链接阿里云存储服务器
            res = oss.put_object_from_file("qutu", img_name, up_load)#执行上传
            if res.status==200:
                url_path="http://qutu.oss-cn-beijing.aliyuncs.com/"+img_name #阿里云存储url地址
                tx.execute("insert into pic (title,url) values (%s,%s)",(item['title'][0],url_path))
                log.msg("Item stored in db: %s" % item, level=log.DEBUG)
            else:
                log.msg("上传失败：%s" % item, level=log.DEBUG)
     
   
            
    def handle_error(self, e):
        log.err(e)