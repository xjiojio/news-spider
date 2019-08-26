from scrapy import cmdline
from news.news.ipProxy import IpProxy

# 先爬取新的代理，避免正在运行的爬虫没有代理可用
# 删除不可用代理
# proxy = IpProxy()
# proxy.get_free_ip()
# proxy.delete_invalid_ip()

# 开始爬虫
cmdline.execute("scrapy crawl sina -o data/out.csv".split())
