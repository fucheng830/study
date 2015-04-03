# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html

import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=["scrapy", 'crawl','doubanmovie'])
    #scrapy.cmdline.execute(argv=["scrapy", 'crawl','doubanmovie','-o','items.json'])
    #scrapy.cmdline.execute(argv=["scrapy", 'shell','http://doc.scrapy.org/en/latest/_static/selectors-sample1.html'])
    
if __name__ == '__main__':
    main()