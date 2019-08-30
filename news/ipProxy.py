import requests
import time
import json
import pymysql
from scrapy.selector import Selector


class IpProxy(object):
    conn = None
    cursor = None

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    page_kuaidaili = 1

    def __init__(self):
        f = open("database.json", "r")
        json_str = f.read()
        f.close()
        json_dic = json.loads(json_str)
        conn = pymysql.connect(
            host=json_dic["MYSQL_HOST"],
            user=json_dic["MYSQL_USER"],
            passwd=json_dic["MYSQL_PASSWD"],
            db=json_dic["MYSQL_DB"],
            charset="utf8")
        cursor = conn.cursor()


    def get_free_ip(self):
        print("get free ip from internet:")
        self.get_kuaidaili("https://www.kuaidaili.com/free/intr/1")

    # 快代理
    def get_kuaidaili(self, url):
        print("url:" + url)
        print("page_kuaidaili:" + str(self.page_kuaidaili))
        response = requests.get(url=url, headers=self.headers)
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
                print('invalid proxy')
                return False

    def is_exist(self, ip):
        sql = "select id from ip_proxy where ip = '%s'" % (ip)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
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
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_ip(self, ip):
        print("delete ip:" + ip)
        sql = "delete from ip_proxy where ip = " + ip
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_all_ip(self):
        print("delete all ip")
        sql = "delete from ip_proxy"
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_invalid_ip(self):
        print("delete invalid ip")
        sql = "select * from ip_proxy"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for var in result:
            proxy_url = '{0}://{1}:{2}'.format(var[3], var[1], var[2])
            available = self.check_ip(var[3], proxy_url)
            if available:
                print("ip " + var[1] + " available")
            else:
                sql = "delete from ip_proxy where ip='%s'" % (var[1])
                self.cursor.execute(sql)
                self.conn.commit()
                print("delete ip:" + var[1])

    def __del__(self):
        self.cursor = None
        self.conn.close()
