import requests
import json

api_key = 'api_key'
password = 'password'
shop_url = 'shop_url.myshopify.com'

url = f'https://{api_key}:{password}@{shop_url}/admin/api/2022-01/products.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    products = data['products']
    
    for product in products:
        print(product['title'])
else:
    print('Erro ao obter os produtos:', response.status_code, response.text)
