# -*- coding: UTF-8 -*-

import re
from BeautifulSoup import BeautifulSoup

def twse_get_stock_code_hidden_inputs(response):
    soup = BeautifulSoup(response)
    inputs = soup.findAll('input', {'type': 'hidden'})
    fields = [x['name'] for x in inputs[-3:]]
    values = [x['value'] for x in inputs[-3:]]
    return dict(zip(fields, values))

def stockdog_get_distribution_atype(response):
    ajax_table_index = response.find('ajax_table')
    index = response[ajax_table_index:].find('Atype') + ajax_table_index
    source = response[index: index+50]
    atype = re.search("'([^']+)'", source).group(1)
    return atype

def stockdog_get_distribution(response):
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
