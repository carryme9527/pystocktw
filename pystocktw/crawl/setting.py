# -*- coding: UTF-8 -*-

def stockdog_equity_distribution_atype(sdssessid):
    return {
        'url': 'https://www.stockdog.com.tw/stockdog/index.php',
        'params': {
            'sid': 2330,
            'p': 7,
            'm': 1,
        },
        'headers': {
            'Cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; SDSSESSID=%s;' % sdssessid,
        },
        'encoding': 'UTF-8',
    }

def stockdog_equity_distribution(sdssessid, atype, sid, _type):
    return {
        'url': 'https://www.stockdog.com.tw/stockdog/ajax.php',
        'params': {
            'Atype': atype,
            'sid': sid,
            'type': _type,
        },
        'headers': {
            'Cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; SDSSESSID=%s;' % sdssessid,
        },
        'encoding': 'UTF-8',
    }

def twse_stock_code_hidden_inputs(stock_type):
    return {
        'url': 'http://mops.twse.com.tw/mops/web/ajax_t51sb01',
        'data': {
            'encodeURIComponent': 1,
            'step': 1,
            'firstin': 1,
            'typek': stock_type,
            'code': '',
        },
    }

def twse_stock_code(data):
    return {
        'url': 'http://mops.twse.com.tw/server-java/t105sb02',
        'data': data,
    }

def twse_equity_distribution_for_cache():
    return {
        'url': 'http://www.tdcc.com.tw/smWeb/QryStock.jsp',
    }

def twse_equity_distribution(sca_date, sid):
    return {
        'url': 'http://www.tdcc.com.tw/smWeb/QryStock.jsp',
        'data': {
            'SCA_DATE': sca_date,
            'StockNo': sid,
            'SqlMethod': 'StockNo',
            'sub': u'查詢'.encode('big5'),
        },
    }
