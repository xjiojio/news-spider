from scrapy import cmdline
from news.news.ipProxy import IpProxy

cmdline.execute("scrapy crawl sina".split())
# proxy = IpProxy()
# proxy.get_free_ip()
