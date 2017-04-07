# -*- coding: UTF-8 -*-

from nose.tools import *
from sessionid import stockdog_session_id, stockdog_chrome_version
from pystocktw.crawl import util, setting
from pystocktw.parse import helper

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_stockdog_equity_distribution():
    req_config = setting.stockdog_equity_distribution_atype(stockdog_session_id, stockdog_chrome_version)
    response = util.get(**req_config)
    atype = helper.stockdog_equity_distribution_atype(response)

    for _type in [1, 2, 3]:
        req_config = setting.stockdog_equity_distribution(stockdog_session_id, atype, 2330, _type)
        response = util.get(**req_config)
        headers, data = helper.stockdog_equity_distribution(response)

# csv
def test_twse_code():
    for typek in ['sii', 'otc']:
        req_config = setting.twse_stock_code_hidden_inputs('sii')
        response = util.post(**req_config)
        payload = helper.twse_stock_code_hidden_inputs(response)

        req_config = setting.twse_stock_code(payload)
        response = util.post(**req_config)

def test_twse_equity_distribution():
    req_config = setting.twse_equity_distribution_for_cache()
    response = util.get(**req_config)

    req_config = setting.twse_equity_distribution('20160401', 2330)
    response = util.post(**req_config)
    helper.twse_equity_distribution(response)

    req_config = setting.twse_equity_distribution('20170331', 2330)
    response = util.post(**req_config)
    helper.twse_equity_distribution(response)

# csv
def test_twse_warrant_info():
    for r in [1, 2]:
        req_config = setting.twse_warrant_info_hidden_inputs(r)
        response = util.post(**req_config)
        payload = helper.twse_warrant_info_hidden_inputs(response)

        req_config = setting.twse_warrant_info(payload)
        response = util.post(**req_config)

    req_config = setting.twse_warrant_info_expired_hidden_inputs(1, '8903', '8903')
    response = util.post(**req_config)
    payload = helper.twse_warrant_info_hidden_inputs(response)

    req_config = setting.twse_warrant_info(payload)
    response = util.post(**req_config)

    req_config = setting.twse_warrant_info_expired_hidden_inputs(2, '9301', '9301')
    response = util.post(**req_config)
    payload = helper.twse_warrant_info_hidden_inputs(response)

    req_config = setting.twse_warrant_info(payload)
    response = util.post(**req_config)

def test_twse_warrant_cancel():
    req_config = setting.twse_warrant_cancel()
    response = util.get(**req_config)
    headers, data = helper.twse_warrant_cancel(response)

# csv
def test_twse_warrant_institution():
    for select2 in ['0999','0999P', '0999C', '0999B', '0999X', '0999Y']:
        req_config = setting.twse_warrant_institution('101/05/02', select2)
        response = util.post(**req_config)

        req_config = setting.twse_warrant_institution('106/04/05', select2)
        response = util.post(**req_config)
