import requests
import base64

api_key = 'api_key'
password = 'password'
shop_url = 'shop_url.myshopify.com'

upload_url = f'https://{api_key}:{password}@{shop_url}/admin/api/2022-01/'

image_paths = ['Caminho/do/produto.jpg', 'Caminho/do/produto.jpg', 'Caminho/do/produto.jpg']

for image_path in image_paths:
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    image_data = {
        'image': {
            'attachment': encoded_image
        }
    }

    upload_endpoint = 'products/8132715512020/images.json'  

    
    response = requests.post(upload_url + upload_endpoint, json=image_data)

    if response.status_code == 200:
        print(f'Imagem {image_path} carregada com sucesso.')
    else:
        print(f'Erro ao carregar a imagem {image_path}:', response.status_code, response.text)
