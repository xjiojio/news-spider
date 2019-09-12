# -*- coding: utf-8 -*-
import pymysql
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        f = open("database.json", "r")
        json_str = f.read()
        f.close()
        json_dic = json.loads(json_str)
        self.conn = pymysql.connect(
            host=json_dic["MYSQL_HOST"],
            user=json_dic["MYSQL_USER"],
            passwd=json_dic["MYSQL_PASSWD"],
            db=json_dic["MYSQL_DB"],
            charset="utf8mb4")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 查询是否录入数据库
        sql = "select news_id, category from allNews where url='%s'" % (item['url'])
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            print("news exist:" + item['url'])
            if result[1].find(item['category']) != -1:
                print("category exist:" + item['category'])
            else:
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
        newcursor = self.conn.cursor()
        print("add category:" + item['category'])
        new_category = result[1] + "," + item['category']
        print("new category:" + new_category)
        sql = "update allNews set category='{}' where news_id='{}'".format(new_category, result[0])
        newcursor.execute(sql)
        self.conn.commit()
