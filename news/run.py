from scrapy import cmdline
from news.news.ipProxy import IpProxy

cmdline.execute("scrapy crawl sina -o data/out.csv".split())
# proxy = IpProxy()
# proxy.delete_all_ip()
# proxy.get_free_ip()
