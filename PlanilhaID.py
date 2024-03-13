import csv
import requests

api_key = 'b4c290c7e9d9fcc74b3a08aa553789e0'
password = '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'
shop_url = 'totvs-tbne-le-loyn-comercio-de-cosmeticos-ltda.myshopify.com'

all_products = []

last_product_id = None

while True:
    products_url = f'https://{api_key}:{password}@{shop_url}/admin/api/2022-01/products.json'
    if last_product_id:
        products_url += f'?since_id={last_product_id}'

    response = requests.get(products_url)

    if response.status_code == 200:
        data = response.json()
        products = data['products']

        all_products.extend(products)

        if len(products) == 0:
            break
        else:
            last_product_id = products[-1]['id']
    else:
        print('Erro ao obter os produtos:', response.status_code, response.text)
        break

csv_path = 'C:/Users/Win/Pictures/TesteShopify/products.csv'

with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nome do Produto', 'ID do Produto', 'SKU'])
    for product in all_products:
        product_id = product['id']
        product_name = product['title']
        product_sku = product['variants'][0]['sku'] if 'variants' in product and len(product['variants']) > 0 else ''
        writer.writerow([product_name, product_id, product_sku])

print('Arquivo CSV gerado com sucesso.')
