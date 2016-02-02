from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def index():
    # product_ids = [611078,611077,611079]
    product = {
        '611078': 'o nome do produto',
        '611077': 'o nome do produto 2'
    }
    histories = {}
    for product_id, product_name  in product.items():
        r = requests.get('http://www.bondfaro.com.br/ajax/historicoPreco?idu='+str(product_id))
        histories[product_name] = json.loads(r.text)
    return render_template('index.html', histories=histories)

if __name__ == "__main__":
    app.run(debug=True)
