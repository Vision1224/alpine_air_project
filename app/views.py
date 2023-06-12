import json
from flask import Blueprint, request, jsonify, render_template
import pandas as pd

main_blueprint = Blueprint('main', __name__, template_folder='../templates', static_folder='../static')

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        try:
            date = request.form.get('date')
            vendor_name = request.form.get('vendorName')
            csv_file = request.files.get('csvFile')
            csv_data = pd.read_csv(csv_file, encoding='unicode_escape')

            purchase_orders = []
            for _, row in csv_data.iterrows():
                model_number = row['Model Number']
                unit_price = str(row['Unit Price']).strip()
                quantity = row['Quantity']
                purchase_orders.append({
                    'model_number': str(model_number).strip(),
                    'unit_price': float(unit_price),
                    'quantity': int(quantity)
                })

            file_path = 'purchase_orders.json'
            with open(file_path, 'a') as json_file:
                for order in purchase_orders:
                    json.dump(order, json_file)
                    json_file.write('\n')
            return 'Purchase orders submitted successfully.', 200


        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return render_template('index.html')

@main_blueprint.route('/orders_data', methods=['GET'])
def orders_data():
    if request.method == 'GET':
        try:
            with open('purchase_orders.json', 'r') as json_file:
                purchase_orders = [json.loads(line) for line in json_file]
            return jsonify(purchase_orders)
        except Exception as e:
            return jsonify({'error': str(e)}), 400


@main_blueprint.route('/orders', methods=['GET'])
def orders():
    if request.method == 'GET':
        return render_template('orders.html')
