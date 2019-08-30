import sys
from scrapy import cmdline
from news.ipProxy import IpProxy


lids = ['2509', '2510', '2511', '2669', '2512', '2513', '2514', '2515', '2516', '2517', '2518']


def run(option, lid="0"):
    if option == "sina":
        if lid == 0:
            print("please input lid")
        elif lid not in lids:
            print("wrong lid")
        else:
            f = open("./news/spiders/sina_lid.json", "w+")
            json_str = '{"lid": "%s"}' % lid
            f.write(json_str)
            f.close()
            # 开始爬虫
            cmdline.execute("scrapy crawl sina -o data/" + lid + ".csv".split())
            # cmdline.execute("scrapy crawl sina -o data/" + str(lid) + ".csv".split())

            cmdline.execute("scrapy crawl sina".split())
    elif option == "ip":
        proxy = IpProxy()
        # 先爬取新的代理，避免正在运行的爬虫没有代理可用
        proxy.get_free_ip()
        # 删除不可用代理
        proxy.delete_invalid_ip()
        pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        opt = sys.argv[1]
        run(opt)
    elif len(sys.argv) == 3:
        opt = sys.argv[1]
        in_lid = sys.argv[2]
        run(opt, in_lid)
    else:
        print("Not support command!")
        sys.exit()
