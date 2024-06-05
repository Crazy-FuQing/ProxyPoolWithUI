# encoding: utf-8

from .BaseFetcher import BaseFetcher
import requests


class LocalFetcher(BaseFetcher):
    """
    http://192.168.1.143/proxypool.txt
    """

    def fetch(self):
        """
        执行一次爬取，返回一个数组，每个元素是(protocol, ip, port)，portocal是协议名称，目前主要为http
        返回示例：[('http', '127.0.0.1', 8080), ('http', '127.0.0.1', 1234)]
        """

        proxies = []

        # 读取本地代理文件
        html = requests.get('http://192.168.1.143/proxypool.txt',  timeout=10).text
        # print(html.split('\r\n'))
        proxy_list = html.split('\r\n')
        # 删除空元素
        filtered_proxy_list = list(filter(None, proxy_list))

        # 将每个元素转换为(协议,主机,port)的元组形式
        formatted_proxy_list = []
        for proxy in filtered_proxy_list:
            # 分割字符串，获取协议、主机和端口
            parts = proxy.split('://')
            protocol = parts[0] if len(parts) > 1 else ''
            host_port = parts[1].split(':') if len(parts) > 1 else ['', '']
            host = host_port[0]
            port = int(host_port[1]) if len(host_port) > 1 else 0
            
            # 将协议、主机和端口组合成一个元组
            formatted_proxy = (protocol, host, port)
            formatted_proxy_list.append(formatted_proxy)

        proxies.extend(formatted_proxy_list)


        
        return list(set(proxies))
