# -*- coding: utf-8 -*-
import json
import random
import scrapy
import requests
from scrapy import Request
from news.items import NewsItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']

    base_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid={}&k=&num=50&page={}&r={}'

    # 全部、国内、国际、社会、体育、娱乐、军事、科技、财经、股市、美股
    category = {
        '2509': '"news"',
        '2510': '"china"',
        '2511': '"world"',
        '2669': '"society"',
        '2512': '"sports"',
        '2513': '"ent"',
        '2514': '"milite"',
        '2515': '"tech"',
        '2516': '"finance"',
        '2517': '"stock"',
        '2518': '"usstock"',
    }
    #  按上面注释  可修改 这里"2509"代表"全部"类别的新闻
    lid = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("init SinaSpider...")
        f = open("./news/spiders/sina_lid.json", "r")
        lid_json = f.read()
        lid_dic = json.loads(lid_json)
        self.lid = lid_dic['lid']
        # print("lid:" + str(self.lid))
        # exit(0)

    def start_requests(self):

        # 请求接口获得新闻条数计算页数
        page_total = self.get_total_page() // 50
        length = page_total // 250
        for page in range(0, page_total + length):
            r = random.random()
            yield Request(self.base_url.format(self.lid, page, r), callback=self.parse)

    def parse(self, response):
        print("开始爬虫。。。")

        if response.status == 403:
            print("response status:" + str(response.status))
        else:
            res = response.body_as_unicode()
            sites = json.loads(res)
            if len(sites['result']['data']):
                for news in sites['result']['data']:
                    request = scrapy.Request(news['url'], callback=self.parse_detail)
                    request.meta['news'] = news
                    yield request
            else:
                print("请修改lid参数进入下一分类")
                # exit(0)

    def parse_detail(self, response):
        print("爬取信息。。。")
        item = NewsItem()
        news = response.meta['news']

        item['title'] = news['title']
        item['stitle'] = news['stitle']
        item['ctime'] = news['ctime']
        item['url'] = news['url']
        item['wap_url'] = news['wapurl']
        item['summary'] = news['summary']
        item['wap_summary'] = news['wapsummary']
        item['intro'] = news['intro']
        item['keywords'] = news['keywords']
        item['content'] = ''.join(response.xpath('//*[@id="artibody"]/p/text()').extract()).replace(u'\u3000\u3000', u'\n').replace(u'\xa0\xa0', u'\n').replace(u'\r\n', u'\n').replace(u'\n\r', u'\n').replace(u'\'', u'\\\'').strip()
        if item['content'] == '':
            item['content'] = ''.join(response.xpath('//*[@id="article"]/p/text()').extract()).replace(u'\u3000\u3000',u'\n').replace(u'\xa0\xa0', u'\n').replace(u'\r\n', u'\n').replace(u'\n\r', u'\n').replace(u'\'', u'\\\'').strip()
        item['category'] = self.category[self.lid]

        yield item

    def get_total_page(self):
        r = random.random()
        result = requests.get(self.base_url.format(self.lid, 1, r))
        res = json.loads(result.text)
        total = res['result']['total']

        return total
