# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):

    def open_spider(self, spider):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="qq123456", db="news-spider", charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 查询是否录入数据库
        sql = "select news_id, category from allNews where url='%s'" % (item['url'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            print("news exist:" + str(item['url']))
            self.update_category(item, result)

        else:
            self.insert_news(item)

        return item

    def close_spider(self, spider):
        self.conn.close()

    def insert_news(self, item):
        sql = "insert allNews" + \
              "(title, stitle, ctime, url, wap_url, summary, wap_summary, intro, keywords, content, category) " \
              "VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
                  .format(item['title'], item['stitle'], item['ctime'],
                          item['url'], item['wap_url'], item['summary'],
                          item['wap_summary'], item['intro'], item['keywords'],
                          item['content'], item['category'])
        self.cursor.execute(sql)
        self.conn.commit()

    def update_category(self, item, result):
        cursor = self.conn.cursor()
        print("result:")
        print(result)
        # sql = "update allNews set category='{}'".format(result.category + "," + item['category'])
        # cursor.execute(sql)
        # self.conn.commit()
