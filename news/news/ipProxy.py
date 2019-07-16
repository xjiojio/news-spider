import requests
import time
import pymysql
from scrapy.selector import Selector

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="qq123456", db="news-spider", charset="utf8")
cursor = conn.cursor()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

class IpProxy(object):

    page_kuaidaili = 1

    def get_free_ip(self):
        print("get free ip from internet:")
        self.get_kuaidaili("https://www.kuaidaili.com/free/intr/1")

    # 快代理
    def get_kuaidaili(self, url):
        print("url:" + url)
        print("page_kuaidaili:" + str(self.page_kuaidaili))
        response = requests.get(url=url, headers=headers)
        response = Selector(text=response.text)
        if response:
            ip = response.xpath('//td[@data-title="IP"]/text()').extract()
            port = response.xpath('//td[@data-title="PORT"]/text()').extract()
            type = response.xpath('//td[@data-title="类型"]/text()').extract()

            for i in range(len(ip)):
                type[i] = type[i].lower()
                proxy_url = '{0}://{1}:{2}'.format(type[i], ip[i], port[i])
                available = self.check_ip(type[i], proxy_url)
                is_exist = self.is_exist(ip[i])

                if available and (not is_exist):
                    self.save_ip(ip[i], port[i], type[i])
        else:
            print("tr_list is null")

        if self.page_kuaidaili == 20:
            exit(0)
        time.sleep(5)
        self.page_kuaidaili += 1
        next_url = 'https://www.kuaidaili.com/free/intr/' + str(self.page_kuaidaili)
        if next_url:
            self.get_kuaidaili(next_url)

    # 西刺代理
    def get_xicidaili(self):
        print("xicidaili.com")

    def check_ip(self, type, proxy_url):
        print("now check ip:")
        request_url = 'http://temp.girst.top/ip.php'
        try:
            proxy = {type: proxy_url}
            response = requests.get(url=request_url, proxies=proxy, timeout=5)
        except Exception as e:
            print(e)
            return False
        else:
            code = response.status_code
            if code == 200 or code == 302:
                print("Available:" + proxy_url)
                return True
            else:
                print('invalid ip and port')
                return False

    def is_exist(self, ip):
        sql = "select id from ip_proxy where ip = '%s'" % (ip)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print("ip " + ip + " exist")
            return True
        else:
            return False

    def save_ip(self, ip, port, type):
        type = type.lower()
        proxy_url = '{0}://{1}:{2}'.format(type, ip, port)
        print("save ip_proxy:" + proxy_url)
        sql = "insert ip_proxy(ip, port, type) VALUES('{0}', '{1}', '{2}')".format(
                ip, port, type
            )
        cursor.execute(sql)
        conn.commit()

    def delete_ip(self, ip):
        print("delete ip:" + ip)
        sql = "delete from ip_proxy where ip = " + ip
        cursor.execute(sql)
        conn.commit()

    def delete_all_ip(self):
        sql = "delete from ip_proxy"
        cursor.execute(sql)
        conn.commit()
