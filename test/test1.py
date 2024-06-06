import requests
from bs4 import BeautifulSoup
import re
import base64

class ProxyScraper:
    @staticmethod
    def freeProxy21():
        # 定义要爬取的URL
        url = 'http://free-proxy.cz/en/proxylist'
        # 设置请求头，模拟浏览器请求
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # 发送GET请求获取页面内容
        response = requests.get(url, headers=headers, timeout=10)
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找分页器元素，获取最大页码
        paginator = soup.find('div', class_='paginator')
        max_page = max([int(a.text) for a in paginator.find_all('a') if a.text.isdigit()])
        print(f'Max Page: {max_page}')

        # 遍历所有页面
        for page in range(1, max_page + 1):
            # 构造每一页的URL
            page_url = f'{url}/main/{page}'
            # 发送GET请求获取该页的内容
            response = requests.get(page_url, headers=headers, timeout=10)
            # 使用BeautifulSoup解析该页的HTML内容
            soup = BeautifulSoup(response.text, 'html.parser')

            # 查找所有代理列表的行
            rows = soup.select('table#proxy_list tbody tr')
            for row in rows:
                # 查找包含代理IP编码的script标签
                script = row.find('td', class_='left', text=re.compile('decode'))
                if script:
                    # 提取并解码代理IP
                    proxy_ip_encoded = re.search(r'decode\("(.+)"\)', script.text).group(1)
                    proxy_ip = base64.b64decode(proxy_ip_encoded).decode('utf-8')
                    # 查找端口号
                    port = row.find('td', class_='left').find_next_sibling('td').find('span').text
                    # 组合成代理字符串
                    proxy = f'{proxy_ip}:{port}'
                    print(proxy)
                    # 生成器返回代理
                    yield proxy

# Example usage
if __name__ == '__main__':
    # 创建代理爬取器实例
    scraper = ProxyScraper()
    # 遍历生成的代理并打印
    for proxy in scraper.freeProxy21():
        print(proxy)
