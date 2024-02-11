import requests
import numpy as np

# URL do seu endpoint Flask
url = 'http://localhost:5000/predict'
features = np.random.rand(201)

# Converter o array NumPy em uma lista Python
features_list = features.tolist()
# Dados que você deseja enviar no formato JSON
data = {
    'features': features_list
    # Adicione mais dados conforme necessário
}

# Enviar a solicitação POST com os dados
response = requests.post(url, json=data)

# Verificar o status da resposta
if response.status_code == 200:
    # Se a solicitação foi bem-sucedida, imprima as previsões recebidas do servidor
    print(response.json())
else:
    # Se ocorreu um erro, imprima a mensagem de erro
    print('Erro:', response.text)
