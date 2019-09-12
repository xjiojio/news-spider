# -*- coding: utf-8 -*-
import requests
import json
import pymysql
from scrapy.selector import Selector


def get_url_item(last_news_id):
    cursor = conn.cursor()
    sql = "select news_id,url from allNews where content = '' and news_id>{0}".format(last_news_id)
    cursor.execute(sql)
    item = cursor.fetchone()
    print(item)
    return item


def get_content(news):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    response = requests.get(url=news[1], headers=headers)
    response.encoding = 'utf-8'
    response = Selector(text=response.text)
    if response:
        content = ''.join(response.xpath('//*[@id="artibody"]/p/text()').extract()).replace(u'\u3000\u3000',
                                                                                            u'\n').replace(u'\xa0\xa0',
                                                                                                           u'\n').replace(
            u'\r\n', u'\n').replace(u'\n\r', u'\n').replace(u'\'', u'\\\'').strip()
        if content == '':
            content = ''.join(response.xpath('//*[@id="article"]/p/text()').extract()).replace(u'\u3000\u3000',
                                                                                               u'\n').replace(
                u'\xa0\xa0', u'\n').replace(u'\r\n', u'\n').replace(u'\n\r', u'\n').replace(u'\'', u'\\\'').strip()
            print("content2:" + content)
        else:
            print("content1:" + content)

        cursor = conn.cursor()
        sql = "update allNews set content='{0}' where news_id={1}".format(content, news[0])
        cursor.execute(sql)
        conn.commit()


f = open("../../database.json", "r")
json_str = f.read()
f.close()
json_dic = json.loads(json_str)
conn = pymysql.connect(
    host=json_dic["MYSQL_HOST"],
    user=json_dic["MYSQL_USER"],
    passwd=json_dic["MYSQL_PASSWD"],
    db=json_dic["MYSQL_DB"],
    charset="utf8")

news = None
while(True):
    if news:
        last_news_id = news[0]
    else:
        last_news_id = 1
    news = get_url_item(last_news_id)
    if news:
        get_content(news)
    else:
        break


