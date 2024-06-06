import requests

def get_proxy():
    url = 'http://zltiqu.pyhttp.taolop.com/getip?count=1&neek=13873&type=2&yys=0&port=2&sb=&mr=2&sep=0'
    proxy_json = requests.get(url=url).json()
    print('获取的代理:', proxy_json)

    ip = proxy_json['data'][0]['ip']
    port = str(proxy_json['data'][0]['port'])

    proxies = {
        # "http": "http://" + ip + ':' + port,
        "https": "http://" + ip + ':' + port,
    }
    return proxies


if __name__ == '__main__':
    proxies = get_proxy()
    print('代理:', proxies)

    # 使用代理发送请求
    response = requests.get(url='https://www.baidu.com', proxies=proxies)
    print(response.text)