# -*- coding: UTF-8 -*-

from nose.tools import *
from pystocktw.crawl import util, setting
from pystocktw.parse import helper

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_stockdog():
    sdssessid = ''

    req_config = setting.stockdog_get_distribution_atype(sdssessid)
    response = util.get(**req_config)
    atype = helper.stockdog_get_distribution_atype(response)

    req_config = setting.stockdog_get_distribution(sdssessid, atype, 2330, 2)
    response = util.get(**req_config)
    headers, data = helper.stockdog_get_distribution(response)

def test_twse_code_sii():
    req_config = setting.twse_get_stock_code_hidden_inputs('sii')
    response = util.post(**req_config)
    payload = helper.twse_get_stock_code_hidden_inputs(response)

    req_config = setting.twse_get_stock_code(payload)
    response = util.post(**req_config)

def test_twse_code_otc():
    req_config = setting.twse_get_stock_code_hidden_inputs('otc')
    response = util.post(**req_config)
    payload = helper.twse_get_stock_code_hidden_inputs(response)

    req_config = setting.twse_get_stock_code(payload)
    response = util.post(**req_config)
