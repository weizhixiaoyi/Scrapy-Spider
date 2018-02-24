# -*- coding: utf-8 -*-
from videoSpider.items import VideospiderItem
from scrapy import Spider,Request
import urllib.request
import json
import re
class VideoSpider(Spider):
    name = 'video'
    allowed_domains = ['www.ljabc.com.cn']

    #因为视频是内部专属，网页端不可浏览，后发现手机端可以观看，因此模拟手机登陆。抓包工具采用Charles。
    # DEFAULT_REQUEST_HEADERS = {
    #     'User-Agent': 'HBuilder/4.2.9.0 (iPhone; iOS 11.3; Scale/2.00)'
    # }
    def start_requests(self):
        phone='18692083764'
        password='Test123456'
        loginUrl='http://app.ljabc.com.cn/app/userapp/userAppLogin_new.html?password='+password+'&phone='+phone
        yield Request(url=loginUrl, callback=self.parse)

    def parse(self, response):
        item=VideospiderItem()#item包括课程名称courseName、课程中各视频名称videoName，视频下载链接video

        #获取课程真实链接
        data = json.loads(response.text)#获取登陆信息
        courseUrl = 'http://www.ljabc.com.cn/user/toCourseDetail.html?courseId=691604'#需抓取的课程主页面
        courseId_ = re.search('courseId=', courseUrl).span()
        courseId = courseUrl[courseId_[1]:] #寻找courseId 即上述691604
        realCourseUrl = 'http://app.ljabc.com.cn/app/classRoom/getCourseByCourseIdForProto.html?courseId=' + courseId + '&sessionId=' +data['loginInfo']['sessionId']

        #获取课程信息
        course_Response = urllib.request.urlopen(realCourseUrl)
        course_Data = json.loads(course_Response.read().decode('utf-8'))

        item['courseName']=course_Data['result']['lineContent']['videoName']
        #分析课程中信息，找出video真实下载链接
        for video in course_Data['result']['chapterList']:
            video_ID = video['path']#课程信息中video路径
            video_Url = video_ID + '?sessionId=EBCB02C992585EFE79C425B24C1F0860&source=0'#video真实下载链接
            item['videoName']=video['detail']
            item['video']=video_Url
            yield item