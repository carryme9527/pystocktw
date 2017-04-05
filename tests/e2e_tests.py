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

    req_config = setting.stockdog_equity_distribution(stockdog_session_id, atype, 2330, 2)
    response = util.get(**req_config)
    headers, data = helper.stockdog_equity_distribution(response)

def test_twse_code_sii():
    req_config = setting.twse_stock_code_hidden_inputs('sii')
    response = util.post(**req_config)
    payload = helper.twse_stock_code_hidden_inputs(response)

    req_config = setting.twse_stock_code(payload)
    response = util.post(**req_config)

def test_twse_code_otc():
    req_config = setting.twse_stock_code_hidden_inputs('otc')
    response = util.post(**req_config)
    payload = helper.twse_stock_code_hidden_inputs(response)

    req_config = setting.twse_stock_code(payload)
    response = util.post(**req_config)

def test_twse_equity_distribution():
    req_config = setting.twse_equity_distribution_for_cache()
    response = util.get(**req_config)
    req_config = setting.twse_equity_distribution('20170331', 2330)
    response = util.post(**req_config)
    helper.twse_equity_distribution(response)

def test_twse_warrant_info():
    req_config = setting.twse_warrant_info_hidden_inputs()
    response = util.post(**req_config)
    payload = helper.twse_warrant_info_hidden_inputs(response)

    req_config = setting.twse_warrant_info(payload)
    response = util.post(**req_config)
