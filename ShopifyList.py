import requests
import json

api_key = 'b4c290c7e9d9fcc74b3a08aa553789e0'
password = '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'
shop_url = 'totvs-tbne-le-loyn-comercio-de-cosmeticos-ltda.myshopify.com'

url = f'https://{api_key}:{password}@{shop_url}/admin/api/2022-01/products.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    products = data['products']
    
    for product in products:
        print(product['title'])
else:
    print('Erro ao obter os produtos:', response.status_code, response.text)
