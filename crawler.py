import requests
import json

products = [611078,611077,611079]
for product in products:
    print product
    r = requests.get('http://www.bondfaro.com.br/ajax/historicoPreco?idu='+str(product))
    history = json.loads(r.text)
    for price in history['historicos']:
        print "{0} - {1}".format(str(price['data']), str(price['precomax']))
