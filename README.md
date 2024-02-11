Projeto de Manutenção Preditiva com Aprendizado de Máquina

Este projeto visa implementar um sistema de manutenção preditiva em um ambiente industrial, utilizando técnicas de aprendizado de máquina para identificar padrões nos dados coletados dos sensores de equipamentos industriais. O sistema permite prever a necessidade de manutenção com base em indicadores de desempenho em tempo real, ajudando a evitar falhas não planejadas e reduzir os custos de manutenção.

Descrição do Projeto
Este projeto é uma implementação de um sistema de manutenção preditiva utilizando aprendizado de máquina. Ele inclui as seguintes etapas:

Exploração e Pré-processamento dos Dados
Treinamento e Avaliação do Modelo
Cada etapa é realizada em um notebook Jupyter separado, que está disponível na pasta "notebooks" deste repositório.

Instruções de Configuração e Execução
Para executar este projeto, siga estas etapas:

Clone o repositório:

bash
Copy code
git clone <https://github.com/alexfloripavieira/projeto_manutencao_preditiva_alexsander_vieira.git>
Instale as dependências:

Copy code
pip install -r requirements.txt
Navegue até a pasta "notebooks" e execute os notebooks Jupyter para cada etapa do projeto.

Siga as instruções em cada notebook para explorar os dados, treinar o modelo, avaliar o modelo e implantá-lo.

Após a etapa de Treinamento e Avaliação do Modelo, execute o arquivo `App.py` no terminal para iniciar o servidor Flask que irá lidar com as solicitações de predição.
bash
Copy code
python3 App.py

Uma vez que o servidor esteja em execução, você pode enviar dados para predição executando o arquivo `enviar_dados.py` no terminal.
bash
Copy code
python3 enviar_dados.py

Conteúdo do Repositório
notebooks/: Contém os notebooks Jupyter para cada etapa do projeto.
dados/: Contém os arquivos de dados necessários para treinar e testar o modelo.
modelos/: Contém os arquivos de modelo treinado.
README.md: Este arquivo que fornece uma visão geral do projeto e instruções de configuração e execução.
Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, por favor, abra uma issue ou envie um pull request.

Licença
Este projeto está licenciado sob a Licença MIT.
