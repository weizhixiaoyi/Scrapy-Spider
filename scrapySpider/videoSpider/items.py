# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VideospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    courseName=scrapy.Field()#课程名称
    videoName=scrapy.Field()#视频名称
    video=scrapy.Field()#视频下载链接