#!/usr/bin/env python

import scraperwiki
import requests
import json
import re

products = ['611077', '611078', '613850', '597260', '610882']
for product in products:
    print "crawler product {0}".format(product)
    r = requests.get('http://www.bondfaro.com.br/ajax/historicoPreco?idu='+product)
    history = json.loads(r.text)
    for price in history['historicos']:
        unique_keys = [ 'idp', 'date']
        idp = str(price['idPu'])
        date = re.sub("(\d)\/(\d)\/(\d)", "\2/\1/\3", price['data'])
        data = { 'idp':idp, 'date':date, 'price_min':price['precomin'], 'price_avg':price['precomed'], 'price_max':price['precomax'],}
        scraperwiki.sql.save(unique_keys, data)
