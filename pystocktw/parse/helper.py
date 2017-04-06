# -*- coding: UTF-8 -*-

import re
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup

def html_unescape(text):
    h = HTMLParser()
    return h.unescape(text)

def twse_stock_code_hidden_inputs(response):
    soup = BeautifulSoup(response)
    inputs = soup.findAll('input', {'type': 'hidden'})
    fields = [x['name'] for x in inputs[-3:]]
    values = [x['value'] for x in inputs[-3:]]
    return dict(zip(fields, values))

def stockdog_equity_distribution_atype(response):
    ajax_table_index = response.find('ajax_table')
    index = response[ajax_table_index:].find('Atype') + ajax_table_index
    source = response[index: index+50]
    atype = re.search("'([^']+)'", source).group(1)
    return atype

def stockdog_equity_distribution(response):
    soup = BeautifulSoup(response)

    def get_headers(thead):
        headers = [thead.findAll('tr')[1].find('th').text] # month
        headers.extend([x.text for x in thead.findAll('tr')[2].findAll('th')]) # buckets
        return headers

    def get_data(tbody):
        data = []
        for row in tbody.findAll('tr'):
            row = [x.text for x in row.findAll('td')]
            data.append(row)
        return data

    headers = get_headers(soup.find('thead'))
    data = get_data(soup.find('tbody'))
    return headers, data

def twse_equity_distribution(response):
    table = BeautifulSoup(response).findAll('table')[-2]

    def get_headers(table):
        return [x.text for x in table.find('tr', { 'class': 'bwl9' }).findAll('td')]

    def get_data(table):
        data = []
        for row in table.findAll('tr')[1:-1]:
            data.append([x.text for x in row.findAll('td')])
        return data

    return get_headers(table), get_data(table)

def twse_warrant_info_hidden_inputs(response):
    soup = BeautifulSoup(response)
    inputs = soup.findAll('input', {'type': 'hidden'})
    fields = [x['name'] for x in inputs[-3:]]
    values = [x['value'] for x in inputs[-3:]]
    return dict(zip(fields, values))

def twse_warrant_cancel(response):
    table = BeautifulSoup(response).findAll('table')[9]

    def get_headers(table):
        return [x.text for x in table.findAll('th')]

    def get_data(table):
        data = []
        for row in table.findAll('tr')[1:]:
            data.append([x.text for x in row .findAll('td')])
        return data

    return get_headers(table), get_data(table)
