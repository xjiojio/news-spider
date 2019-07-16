# -*- coding: utf-8 -*-
import json
import random
import scrapy
from scrapy import Request
from news.items import NewsItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']

    base_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid={}&k=&num=50&page={}&r={}'

    # 全部、国内、国际、社会、体育、娱乐、军事、科技、财经、股市、美股
    lids = ['2509', '2510', '2511', '2669', '2512', '2513', '2514', '2515', '2516', '2517', '2518']
    index = 0
    page = 1

    def start_requests(self):
        #  可修改  这里设置爬取100页
        page_total = 100
        for page in range(1, page_total + 1):
            #  按上面注释  可修改 这里"2509"代表"全部"类别的新闻
            lid = "2509"
            r = random.random()
            yield Request(self.base_url.format(lid, page, r), callback=self.parse)

    def parse(self, response):
        print("开始爬虫。。。")
        print(self.url)

        res = response.body_as_unicode()
        if response.status == 403:
            print("response status:" + str(response.status))
        else:
            sites = json.loads(res)
            if len(sites['result']['data']):
                for news in sites['result']['data']:
                    request = scrapy.Request(news['url'], callback=self.parse_detail)
                    request.meta['news'] = news
                    yield request
            else:
                print("data null,url with new lid:")
                self.index += 1
                if self.index > len(self.lids):
                    print("finish")
                    return
                self.page = 0
                self.url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=%s&num=50&page=%d&r=%f' % (self.lids[self.index], self.page, random.random())
                print(self.url)
                yield scrapy.Request(self.url, callback=self.parse)
                print("进入下一分类")

        pass

    def parse_detail(self, response):
        # time.sleep(random.randint(3, 7))
        print("爬取信息。。。")
        item = NewsItem()
        news = response.meta['news']

        item['title'] = news['title']
        item['create_time'] = news['ctime']
        item['url'] = news['url']
        item['wap_url'] = news['wapurl']
        item['summary'] = news['summary']
        item['wap_summary'] = news['wapsummary']
        item['intro'] = news['intro']
        item['keywords'] = news['keywords']
        item['content'] = ''.join(response.xpath('//*[@id="artibody"]/p/text()').extract()).replace(u'\u3000\u3000', u'\n').replace(u'\xa0\xa0', u'\n').replace(u'\r\n', u'\n').replace(u'\n\r', u'\n').strip()
        item['source'] = '新浪'
        # item['category'] = 'category'

        yield item
        pass
