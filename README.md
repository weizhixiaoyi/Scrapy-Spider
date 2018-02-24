# scrapySpider

### 1.寻找真实视频链接

因为视频为内部专属视频，普通注册用户用浏览器不能观看，找不到相应下载链接。

![photo1](https://github.com/XiaoYiii/scrapySpider/blob/master/photos/photo1.png)

后发现通过手机端可以观看，因此模拟模拟手机登陆，采用Charles进行抓包。登陆成功后可获取其sessionId。

	"loginInfo": {
		"result": "4",
		"sessionId": "EBCB02C992585EFE79C425B24C1F0860",
		"userId": "18692083764",
		"userStatus": "0",
		"msg": "登陆成功！"
	}
[此](http://www.ljabc.com.cn/user/toCourseDetail.html?courseId=691604) 课程信息如下所示，包含课程名称、视频信息、视频路径等信息。

	"isTrainLimit": 0,
	"result": {
		"lineContent": {
			"adaptObject": "1",
			"detail": "<p class=\"p1\">\n\t指标平台简介，数据接入，指标创建及查询，报表创建和查询，看板的创建及查询\n<\/p>",
			"videoUrl": "http://video.ljabc.com.cn/upload/cdn_video/image/PIC_0000008082.jpg",
			"videoPath": "http://video.ljabc.com.cn/upload/cdn_video/file_0000008084.mp4",
			"videoName": "指标平台简介及全流程案例分享",
			"typeName": "10",
			"currentTime": "2018-02-24 19:52:17",
			"id": "691604",
			"countdown": "",
			"yhPrice": "0",
			"address": "",
			"couponStatus": "0",
			"saleQty": "0",
			"playQty": "403",
			"sjPrice": "0",
			"trainLimit": "",
			"effectiveTime": "永久",
			"teacher": "钱明霞",
			"courseType": "10"
		},
		"dailyLesson": "1",
		"chapterList": [{
			"id": "4904",
			"detail": "指标平台简介",
			"name": "指标平台简介及全流程案例分享（一）",
			"path": "http://video.ljabc.com.cn/upload/cdn_video/file_0000008084.mp4",
			"lookDetail": "1"
		}, {
			"id": "4905",
			"detail": "全流程案例分享",
			"name": "指标平台简介及全流程案例分享（一）",
			"path": "http://video.ljabc.com.cn/upload/cdn_video/file_0000008085.mp4",
			"lookDetail": "0"
		}]
	},
	"isShareCourse": 0,
	"code": "200"
其中视频下载链接为[http://video.ljabc.com.cn/upload/cdn_video/file_0000008084.mp4?sessionId=EBCB02C992585EFE79C425B24C1F0860&source=0](http://video.ljabc.com.cn/upload/cdn_video/file_0000008084.mp4?sessionId=EBCB02C992585EFE79C425B24C1F0860&source=0)。真实视频链接格式为path+'?sessionId='+sessionId+'&source=0'，找到真实视频链接即可下载视频。

![photo2](https://github.com/XiaoYiii/scrapySpider/blob/master/photos/photo2.png)

### 2.利用scrapy爬取视频

运行程序`scrapy crawl video`

![photo3](https://github.com/XiaoYiii/scrapySpider/blob/master/photos/photo3.png)

程序根据课程名称创建文件夹，并下载课程视频，视频名称根据视频简介命名。最后成功下载课程中视频，因视频较大，所以没有上传视频到GitHub。

![photo4](https://github.com/XiaoYiii/scrapySpider/blob/master/photos/photo4.png)