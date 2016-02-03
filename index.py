from flask import Flask, render_template
import requests
import json
import pdb
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', histories=get_product_histories())

@app.route("/graph")
def graph():
    histories = get_product_histories()
    series = {}
    for product_name, history_product in histories.items():
        series[product_name] = {}
        dates = []
        prices = []
        for record in history_product['historicos']:
            dates.append(record['data'])
            prices.append(record['precomax'])
        series[product_name]['dates'] = dates
        series[product_name]['prices'] = prices
    # pdb.set_trace()
    return render_template('graph.html', series=series)

@app.route("/about")
def about():
    return render_template('about.html')

def get_products():
    return {
        '611077': 'Joy H222TV',
        '611078': 'G4 H815P',
        '613850': 'G4 Beat H736',
        '597260': 'G3 D855',
        '610882': 'Prime Plus H502TV '
    }

def get_product_histories():
    products = get_products()
    histories = {}
    for product_id, product_name  in products.items():
        r = requests.get('http://www.bondfaro.com.br/ajax/historicoPreco?idu='+str(product_id))
        histories[product_name] = json.loads(r.text)
    return histories

if __name__ == "__main__":
    app.run(debug=True)
