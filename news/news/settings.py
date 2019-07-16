# -*- coding: utf-8 -*-

# Scrapy settings for news project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'

# 自己加的
HTTPERROR_ALLOWED_CODES = [403]
FEED_EXPORT_FIELDS = [
    'title',
    'create_time',
    'url',
    'wap_url',
    'summary',
    'wap_summary',
    'intro',
    'keywords',
    'content',
    'source',
    'cate']

PROXIES = [
    'http://148.66.23.131:8080',
    'http://109.160.111.168:8080',
    'http://115.53.23.81:9999',
    'http://212.64.51.13:8888',
    'http://111.13.134.23:80',
    'http://114.55.103.83:8088',
    'http://27.203.165.98:8060',
    'http://60.216.60.234:8060',
    'http://123.207.68.166:1080',
    'http://183.88.212.184:8080',
    'http://169.239.46.73:32231',
    'http://101.37.118.54:8888',
    'http://47.252.15.111:3128',
    'http://45.77.32.152:80',
    'http://218.60.8.99:3129',
    'http://1.186.63.130:39142',
    'http://117.191.11.112:8080',
    'http://60.10.22.229:63141',
    'http://137.59.161.162:32372',
    'http://178.32.80.239:8080',
    'http://189.51.98.182:56906',
    'http://41.221.107.168:80',
    'http://142.4.204.85:8080',
    'http://39.137.107.98:8080',
    'http://117.127.0.202:8080',
    'http://36.25.243.50:80',
    'http://182.74.40.146:30909',
    'http://117.191.11.103:80',
    'http://124.41.243.22:47894',
    'http://159.65.140.120:3128',
    'http://200.122.211.26:8080',
    'http://204.29.115.149:8080',
    'http://114.67.229.212:8080',
    'http://95.9.106.239:808',
    'http://47.75.213.201:80',
    'http://207.180.226.111:8080',
    'http://123.206.30.254:808',
    'http://5.160.218.71:3128',
    'http://197.148.64.194:8080',
    'http://112.17.177.51:8060',
    'http://117.191.11.104:80',
    'http://96.9.87.15:80',
    'http://103.74.108.145:57469',
    'http://105.235.193.94:61386',
    'http://157.119.117.22:35522',
    'http://82.194.235.162:8080',
    'http://125.63.83.42:80',
    'http://58.243.56.148:8060',
    'http://110.74.216.216:53495',
    'http://134.209.1.204:8080',
    'http://82.165.75.254:80',
    'http://31.200.229.104:56471',
    'http://104.248.51.47:8080',
    'http://217.74.161.42:34175',
    'http://124.193.37.5:8888',
    'http://159.138.22.112:80',
    'http://41.205.231.202:8080',
    'http://103.218.2.159:8080',
    'http://197.188.222.163:61636',
    'http://209.97.174.15:3128',
    'http://35.189.90.214:3128',
    'http://117.191.11.107:8080',
    'http://39.137.69.10:80',
    'http://64.193.63.8:80',
    'http://150.109.55.190:83',
    'http://117.191.11.102:80',
    'http://185.148.220.11:8081',
    'http://125.26.99.186:54193',
    'http://112.35.56.134:80',
    'http://77.232.166.153:33574',
    'http://191.240.152.131:80',
    'http://118.190.145.138:9001',
    'http://206.125.41.135:80',
    'http://142.93.248.145:80',
    'http://115.159.31.195:8080',
    'http://112.17.121.88:8060',
    'http://182.61.179.157:8888',
    'http://103.239.253.161:8080',
    'http://178.32.80.233:8080',
    'http://217.182.120.165:8080',
    'http://180.180.152.75:39364',
    'http://43.245.131.124:8080',
    'http://91.106.86.212:8080',
    'http://117.127.16.206:8080',
    'http://178.92.9.210:3128',
    'http://117.191.11.105:8080',
    'http://118.174.65.170:59783',
    'http://203.189.89.82:8080',
    'http://94.242.58.14:10010',
    'http://153.92.5.186:8080',
    'http://94.242.58.142:10010',
    'http://190.152.245.18:8080',
    'http://141.170.5.181:8080',
    'http://118.175.93.94:30613',
    'http://36.74.102.133:8080',
    'http://117.78.34.242:80',
    'http://111.40.84.73:9797',
    'http://92.38.126.189:3128',
    'http://94.242.58.108:1448',
    'http://163.172.181.225:80',
    'http://191.240.152.135:80',
    'http://89.187.200.181:8080',
    'http://27.131.157.94:8080',
    'http://163.204.246.195:9999',
    'http://116.114.19.204:443',
    'http://88.247.158.51:80',
    'http://116.114.19.211:443',
    'http://59.152.98.130:8080',
    'http://39.137.69.6:8080',
    'http://85.196.183.162:8080',
    'http://182.52.131.127:8080',
    'http://68.183.100.171:80',
    'http://91.206.19.193:8081',
    'http://65.52.174.40:80',
    'http://118.174.232.92:45759',
    'http://117.127.0.202:80',
    'http://193.124.184.171:80',
    'http://212.227.10.87:80',
    'http://1.20.101.90:37006',
    'http://128.199.229.157:80',
    'http://42.200.118.202:80',
    'http://104.154.247.127:80',
    'http://47.112.24.110:80',
    'http://101.231.104.82:80',
    'http://124.41.240.207:49623',
    'http://183.63.101.62:55555',
    'http://117.127.16.207:8080',
    'http://167.88.117.209:3128',
    'http://117.191.11.80:8080',
    'http://94.101.141.242:80',
    'http://218.59.139.238:80',
    'http://195.46.168.147:8080',
    'http://117.191.11.109:8080',
    'http://167.88.117.209:8080',
    'http://46.4.102.139:80',
    'http://185.226.65.188:8080',
    'http://185.217.90.139:80',
    'http://165.90.35.206:3128',
    'http://39.96.63.240:80',
    'http://192.99.154.47:8080',
    'http://191.240.152.130:80',
    'http://114.30.75.215:30080',
    'http://83.97.111.202:41258',
    'http://218.58.193.98:8060',
    'http://114.225.171.176:8060',
    'http://209.97.174.15:8080',
    'http://101.89.128.34:80',
    'http://125.27.251.82:50574',
    'http://39.137.69.7:80',
    'http://35.225.208.4:80',
    'http://94.242.58.14:1448',
    'http://94.242.58.108:10010',
    'http://117.191.11.76:80',
    'http://159.138.20.247:80',
    'http://117.191.11.111:8080',
    'http://210.18.140.146:8080',
    'http://117.191.11.105:80',
    'http://113.88.64.228:8888',
    'http://113.190.253.89:80',
    'http://94.242.59.135:10010',
    'http://202.142.221.131:80',
    'http://92.50.31.125:30455',
    'http://185.226.229.166:8080',
    'http://82.194.235.142:8080',
    'http://103.42.89.69:53281',
    'http://182.52.238.119:40456',
    'http://68.183.99.96:8080',
    'http://203.113.10.153:8080',
    'http://110.77.197.244:8080',
    'http://157.230.254.93:8080',
    'http://39.137.77.66:80',
    'http://103.78.11.18:8080',
    'http://117.191.11.103:8080',
    'http://185.62.190.60:8080',
    'http://179.43.105.143:8080',
    'http://151.80.36.115:1080',
    'http://177.185.114.89:53281',
    'http://119.82.252.115:49085',
    'http://94.177.247.221:80',
    'http://84.42.53.44:8080',
    'http://47.244.5.203:8080',
    'http://52.39.101.98:80',
    'http://91.203.224.177:36731',
    'http://47.254.69.158:9999',
    'http://46.63.162.171:8080',
    'http://12.218.209.130:53281',
    'http://222.73.217.7:8080',
    'http://39.137.69.9:80',
    'http://192.117.146.110:80',
    'http://61.238.82.202:8080',
    'http://182.92.219.211:80',
    'http://139.5.71.126:23500',
    'http://101.4.136.34:80',
    'http://185.217.90.143:80',
    'http://39.137.69.7:8080',
    'http://39.137.168.230:80',
    'http://217.182.120.167:8080',
    'http://131.117.214.28:57514',
    'http://94.253.19.231:8080',
    'http://39.108.7.139:808',
]
# 自己加的


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'news (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'news.middlewares.NewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'news.middlewares.ProxyMiddleware': 543,
   'news.middlewares.UAMiddleware': 544,
   # 'news.middlewares.NewsDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'news.pipelines.NewsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
