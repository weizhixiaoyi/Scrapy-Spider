# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request
import os
class VideospiderPipeline(object):
    def process_item(self, item, spider):
        if not os.path.exists(item['courseName']):
            os.mkdir(item['courseName'])#如果文件名不存在则创建文件，文件名名称为课程名称
        print(item['videoName'],item['video'])
        urllib.request.urlretrieve(item['video'], '%s/%s.mp4'%(item['courseName'],item['videoName']))#下载视频并保存在相应文件夹之中
        return item
