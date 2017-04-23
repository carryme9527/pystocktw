# -*- coding: UTF-8 -*-

import requests

def get_headers():
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/56.0.2924.87 Safari/537.36')
    }

def wrap_request(func, url, encoding, headers, **args):
    h = get_headers()
    h.update(headers)
    req = func(url, headers=h, **args)
    req.encoding = encoding
    return req.text.encode('utf8')

def get(url, encoding='big5', headers={}, **args):
    assert 'data' not in args.keys()
    return wrap_request(requests.get, url, encoding=encoding, headers=headers, **args)

def post(url, encoding='big5', headers={}, **args):
    assert 'params' not in args.keys()
    return wrap_request(requests.post, url, encoding=encoding, headers=headers, **args)
