# -*- coding: UTF-8 -*-

import datetime

def stockdog_equity_distribution_atype(sdssessid, chrome_version):
    return {
        'url': 'https://www.stockdog.com.tw/stockdog/index.php',
        'params': {
            'sid': 2330,
            'p': 7,
            'm': 1,
        },
        'headers': {
            'Cookie': 'G_AUTHUSER_H=0; G_ENABLED_IDPS=google; SDSSESSID=%s;' % sdssessid,
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s Safari/537.36' % chrome_version,
        },
        'encoding': 'UTF-8',
    }

def stockdog_equity_distribution(sdssessid, atype, sid, _type):
    return {
        'url': 'https://www.stockdog.com.tw/stockdog/ajax.php',
        'params': {
            'Atype': atype,
            'sid': sid,
            'type': _type, # 1, 2, 3
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
            'typek': stock_type, # sii, otc
            'code': '',
        },
    }

def twse_stock_code(data):
    return {
        'url': 'http://mops.twse.com.tw/server-java/t105sb02',
        'data': data,
    }

def tdcc_equity_distribution_for_cache():
    return {
        'url': 'http://www.tdcc.com.tw/smWeb/QryStock.jsp',
    }

def tdcc_equity_distribution(date, sid):
    sca_date = date.strftime('%Y%m%d')
    return {
        'url': 'http://www.tdcc.com.tw/smWeb/QryStock.jsp',
        'data': {
            'SCA_DATE': sca_date, # 2016/04/01
            'StockNo': sid,
            'SqlMethod': 'StockNo',
            'sub': u'查詢'.encode('big5'),
        },
    }

def twse_warrant_info_hidden_inputs(r):
    return {
        'url': 'http://mops.twse.com.tw/mops/web/ajax_t90sb01',
        'data': {
            'encodeURIComponent': 1,
            'step': 1,
            'firstin': 1,
            'off': 1,
            'r': r, # 1, 2
        },
    }

def twse_warrant_info(data):
    return {
        'url': 'http://mops.twse.com.tw/server-java/t105sb02',
        'data': data,
    }

def twse_warrant_info_expired_hidden_inputs(r, sdate, edate):
    sd = '%d%02d' % (sdate.year-1911, sdate.month)
    ed = '%d%02d' % (edate.year-1911, edate.month)
    return {
        'url': 'http://mops.twse.com.tw/mops/web/ajax_t90sb01',
        'data': {
            'encodeURIComponent': 1,
            'step': 1,
            'firstin': 1,
            'off': 1,
            'r': r, # 1, 2
            'rc': 0,
            'start_date': sd, # 8903 (r=1) 9301 (r=2)
            'end_date': ed, # current month
        },
    }

def twse_warrant_cancel():
    return {
        'url': 'http://mops.twse.com.tw/mops/web/t132sb11',
        'encoding': 'UTF-8',
    }

def twse_warrant_listed_institution(date, select2):
    qdate = '%d/%02d/%02d' % (date.year-1911, date.month, date.day)
    return {
        'url': 'http://www.twse.com.tw/ch/trading/fund/T86/T86.php',
        'data': {
            'download': 'csv',
            'qdate': qdate, # 101/05/02
            'select2': select2, # 0999, 0999P, 0999C, 0999B, 0999X, 0999Y
            'sorting': 'by_issue',
        },
    }

def tpex_warrant_counter_institution(se, date):
    if date < datetime.date(2014, 12, 1):
        return tpex_warrant_counter_institution_103(se, date)
    date = '%d/%02d/%02d' % (date.year-1911, date.month, date.day)
    return {
        'url': 'http://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_hedge_download.php',
        'params': {
            'l': 'zh-tw',
            'se': se, # EW, BC
            't': 'D',
            'd': date, # 103/12/01
            's': '0,asc',
        },
    }

def tpex_warrant_counter_institution_103(se, date):
    date = '%d/%02d/%02d' % (date.year-1911, date.month, date.day)
    return {
        'url': 'http://www.tpex.org.tw/web/stock/3insti/daily_trade/3itrade_download.php',
        'params': {
            'l': 'zh-tw',
            'se': se, # EW, BC
            't': 'D',
            'd': date, # 96/04/23
            's': '0,asc',
        },
    }

def taifex_option_daily(commodity, date):
    return {
        'url': 'http://www.taifex.com.tw/chinese/3/3_2_2.asp',
        'data': {
            'commodity_id': commodity,
            'syear': date.year,
            'smonth': date.month,
            'sday': date.day,
        },
        'encoding': 'utf8',
    }
