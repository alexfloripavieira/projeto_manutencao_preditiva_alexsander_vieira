import requests
import numpy as np

# URL do endpoint do servidor Flask
url = 'http://localhost:5000/predict'

# Solicitar ao usuário que digite o número do modelo e o número do "randow"
model_number = int(input("Digite o número do modelo (1 a 5): "))

# Verificar se o número do modelo está no intervalo válido
if model_number < 1 or model_number > 5:
    print("Número do modelo inválido. Por favor, escolha um número entre 1 e 5.")
    exit()


# Gera uma matriz de características de acordo com o 'model_number'
features = np.random.rand(201) if model_number < 4 else np.random.rand(200)
# Converter a matriz NumPy em uma lista de listas Python
features_list = features.tolist()

# Dados que você deseja enviar no formato JSON, incluindo o número do modelo
data = {
    'model_number': model_number,
    'features': features_list
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
