# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    create_time = scrapy.Field()
    url = scrapy.Field()
    wap_url = scrapy.Field()
    summary = scrapy.Field()
    wap_summary = scrapy.Field()
    intro = scrapy.Field()
    keywords = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
    category = scrapy.Field()
    pass
