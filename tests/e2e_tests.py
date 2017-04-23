# -*- coding: UTF-8 -*-

from nose.tools import *
from sessionid import stockdog_session_id, stockdog_chrome_version
from pystocktw.crawl import util, setting
from pystocktw.parse import helper
import datetime

def test_stockdog_equity_distribution():
    req_config = setting.stockdog_equity_distribution_atype(stockdog_session_id, stockdog_chrome_version)
    response = util.get(**req_config)
    atype = helper.stockdog_equity_distribution_atype(response)

    for _type in [1, 2, 3]:
        req_config = setting.stockdog_equity_distribution(stockdog_session_id, atype, 2330, _type)
        response = util.get(**req_config)
        headers, data = helper.stockdog_equity_distribution(response)
        for d in data:
            assert len(headers) == len(d)

# csv
def test_twse_code():
    for typek in ['sii', 'otc']:
        req_config = setting.twse_stock_code_hidden_inputs(typek)
        response = util.post(**req_config)
        payload = helper.twse_stock_code_hidden_inputs(response)

        req_config = setting.twse_stock_code(payload)
        response = util.post(**req_config)

# date
def test_tdcc_equity_distribution():
    req_config = setting.tdcc_equity_distribution_for_cache()
    response = util.get(**req_config)

    for date in [datetime.date(2016, 4, 15), datetime.date(2017, 3, 31)]:
        req_config = setting.tdcc_equity_distribution(date, 2330)
        response = util.post(**req_config)
        headers, data = helper.tdcc_equity_distribution(response)
        for d in data:
            assert len(headers) == len(d)

# date
# csv
def test_twse_warrant_info():
    for r in [1, 2]:
        req_config = setting.twse_warrant_info_hidden_inputs(r)
        response = util.post(**req_config)
        payload = helper.twse_warrant_info_hidden_inputs(response)

        req_config = setting.twse_warrant_info(payload)
        response = util.post(**req_config)


    for date in [datetime.date(1990, 3, 1), datetime.date(2017, 4, 1)]:
        for r in [1, 2]:
            req_config = setting.twse_warrant_info_expired_hidden_inputs(1, date, date)
            response = util.post(**req_config)
            payload = helper.twse_warrant_info_hidden_inputs(response)

            req_config = setting.twse_warrant_info(payload)
            response = util.post(**req_config)

def test_twse_warrant_cancel():
    req_config = setting.twse_warrant_cancel()
    response = util.get(**req_config)
    headers, data = helper.twse_warrant_cancel(response)
    for d in data:
        assert len(headers) == len(d)

# date
# csv
def test_twse_warrant_listed_institution():
    for select2 in ['0999','0999P', '0999C', '0999B', '0999X', '0999Y']:
        for date in [datetime.date(2012, 5, 2), datetime.date(2017, 4, 5)]:
            req_config = setting.twse_warrant_listed_institution(date, select2)
            response = util.post(**req_config)

# date
# csv
def test_tpex_warrant_counter_institution():
    for se in ['EW', 'BC']:
        for date in [datetime.date(2007, 4, 23), datetime.date(2014, 11, 30),
                     datetime.date(2014, 12, 1), datetime.date(2017, 4, 5)]:
            req_config = setting.tpex_warrant_counter_institution(se, date)
            response = util.get(**req_config)

# date
def test_taifex_option_daily():
    req_config = setting.taifex_option_daily('TXO', datetime.date(2001, 12, 24))
    response = util.post(**req_config)
    helper.taifex_option_daily(response)

    date = datetime.date(2005, 3, 28)
    for comm in ['TEO', 'TFO']:
        req_config = setting.taifex_option_daily(comm, date)
        response = util.post(**req_config)
        headers, data = helper.taifex_option_daily(response)
        for d in data:
            assert len(headers) == len(d)

    date = datetime.date(2007, 10, 8)
    for comm in ['GTO', 'XIO']:
        req_config = setting.taifex_option_daily(comm, date)
        response = util.post(**req_config)
        headers, data = helper.taifex_option_daily(response)
        for d in data:
            assert len(headers) == len(d)

    date = datetime.date(2017, 4, 21)
    for comm in ['TXO', 'TEO', 'TFO', 'GTO', 'XIO']:
        req_config = setting.taifex_option_daily(comm, date)
        response = util.post(**req_config)
        headers, data = helper.taifex_option_daily(response)
        for d in data:
            assert len(headers) == len(d)
