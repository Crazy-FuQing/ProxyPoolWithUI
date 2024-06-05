

import re
from pyquery import PyQuery as pq
import requests


def fetch():
    """
    执行一次爬取，返回一个数组，每个元素是(protocol, ip, port)，portocal是协议名称，目前主要为http
    返回示例：[('http', '127.0.0.1', 8080), ('http', '127.0.0.1', 1234)]
    """

    urls = [
        'http://www.66ip.cn/nmtq.php?getnum=9999&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=1&api=66ip',
        'http://www.66ip.cn/nmtq.php?getnum=300&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip',
        'http://www.66ip.cn/mo.php?sxb=&tqsl=10000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=http%3A%2F%2Fwww.66ip.cn%2F%3Fsxb%3D%26tqsl%3D10%26ports%255B%255D2%3D%26ktip%3D%26sxa%3D%26radio%3Dradio%26submit%3D%25CC%25E1%2B%2B%25C8%25A1'
            ]
    # for areaindex in range(10):
    #     for page in range(1, 6):
    #         if areaindex == 0:
    #             url = f'http://www.66ip.cn/{page}.html'
    #         else:
    #             url = f'http://www.66ip.cn/areaindex_{areaindex}/{page}.html'
    #         urls.append(url)


    proxies = []
    ip_regex = re.compile(r'^\d+\.\d+\.\d+\.\d+$')
    port_regex = re.compile(r'^\d+$')

    for url in urls:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36'
        }
        html = requests.get(url, headers=headers, timeout=10).text
        # 使用正则表达式匹配 IP:Port 格式
        pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:(?P<port>\d+)'
        matches = re.findall(pattern, html)

        # 构造结果列表
        result = [('http', match[0], int(match[1])) for match in matches]
        proxies.extend(result)
        
    return list(set(proxies))


print(len(fetch()))