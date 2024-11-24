from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Base URL
BASE_URL = "https://kaxru2bff6.execute-api.us-east-1.amazonaws.com/items"

# PUT: Yeni bir öğe ekleme
def put_item(item_id, name, price):
    url = BASE_URL
    data = {
        "id": item_id,
        "name": name,
        "price": price
    }
    response = requests.put(url, json=data)
    return response

# GET: Tüm öğeleri alma
def get_all_items():
    url = BASE_URL
    response = requests.get(url)
    return response.json()

# GET: Belirli bir öğeyi alma
def get_item(item_id):
    url = f"{BASE_URL}/{item_id}"
    response = requests.get(url)
    return response.json()

# DELETE: Belirli bir öğeyi silme
def delete_item(item_id):
    url = f"{BASE_URL}/{item_id}"
    response = requests.delete(url)
    return response

@app.route('/')
def index():
    items = get_all_items()
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item_id = request.form['item_id']
    name = request.form['name']
    price = request.form['price']
    put_item(item_id, name, price)
    return redirect(url_for('index'))

@app.route('/get_item', methods=['POST'])
def view_item():
    item_id = request.form['item_id']
    item = get_item(item_id)
    return render_template('index.html', items=[item])

@app.route('/delete_item', methods=['POST'])
def remove_item():
    item_id = request.form['item_id']
    delete_item(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
