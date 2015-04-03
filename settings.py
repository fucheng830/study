# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'
SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES={
    'tutorial.Images_pipline.MyImagesPipeline': 1,
    #'tutorial.mongo_pipelines.MongoDBPipeline':300,
    'tutorial.pipelines.DoubanmoivePipeline':400,
}

#LOG_LEVEL='DEBUG'
IMAGES_STORE = './images'
IMAGES_EXPIRES = 90
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'tutorial.contrib.downloadermiddleware.rotate_useragent.RotateUserAgentMiddleware' :500,
    }
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'

COOKIES_ENABLED = None
#MONGODB_SERVER = 'localhost'
#MONGODB_PORT = 27017
#MONGODB_DB = 'python'
#MONGODB_COLLECTION = 'usercollection'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
