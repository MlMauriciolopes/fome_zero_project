# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Através desse aplicativo, você consegue ter uma vasta visão de, como andam o gerenciamento, as classificações, e os melhores lugares para visitar lugares gastronômicos, com um simples toque de botão.

Outra vantangem é que, você pode ter uma boa ideia da cultura local e das avaliações, sem sair de casa, e/ou ir preparado para uma escolha mais acertiva de escolha.

Você foi contratado como um Cientista de Dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um os principais KPIs estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder as necessidades da empresa.

A Fome Zero! possui um modelo de negócio chamado Marketplace, que fazer o intermédio do negócio entre três clientes principais: Cidades, Países e tipos de culinárias. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:

A Visão Geral:

    1. Quantos restaurantes únicos estão registrados?
    2. Quantos países únicos estão registrados?
    3. Quantas cidades únicas estão registradas?
    4. Qual o total de avaliações feitas?
    5. Qual o total de tipos de culinária registrados?

A Visão dos Países:

    1. Qual o nome do país que possui mais cidades registradas?
    2. Qual o nome do país que possui mais restaurantes registrados?
    3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
    4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
    5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
    7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
    8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
    9. Qual o nome do país que possui, na média, a maior nota média registrada?
    10. Qual o nome do país que possui, na média, a menor nota média registrada?
    11. Qual a média de preço de um prato para dois por país?

A Visão de Cidades:

    1. Qual o nome da cidade que possui mais restaurantes registrados?
    2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
    3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
    4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
    6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
    7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
    8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
    
A Visão de restauantes:

    1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    2. Qual o nome do restaurante com a maior nota média?
    3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
    4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
    5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
    6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
    7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
    8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

A Visão de tipos de culinárias:

    1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
    2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
    3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
    4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
    5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
    6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
    7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
    8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
    9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
    10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
    11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
    12. Qual o tipo de culinária que possui a maior nota média?
    13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 2. Premissas assumidas para a análise

    1. A análise foi realizada com dados fornecidos pela própria empresa, para poder alavancar ainda mais o negócio.
    2. Marketplace foi o modelo de negócio assumido.
    3. Os 3 principais visões do negócio foram: Visão de Países. Visão de Cidades e Visão de Tipos de Culinárias distintas.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:

    1. Visão do crescimento da empresa
    2. Visão do crescimento dos restaurantes
    3. Visão do crescimento dos entregadores

Cada visão é representada pelo seguinte conjunto de métricas.

    A Visão dos Países:

    1. Quantidade de restaurantes registrados por país.
    2. Quantidade de cidades registradas por país.
    3. Melhor média de avaliações média por país.
    4. Preço médio de um prato para duas pessoas.

A Visão de Cidades:

    1. Top restaurantes registrados na bas de dados.
    2. Top restaurantes com a média de avaliação acima de 4 estrelas.
    3. Restaurantes com média de avaliação abaixo de 2.5 estrelas.
    4. Top cidades com restaurantes com tipos de culinárias distintas.

A Visão de tipos de culinárias:

    1. Visão geral dos melhores restaurantes dos principais tipos de culinárias.
    2. Top restaurantes da base de dados.
    3. Top 10 melhores tipos de culinárias.
    4. Top tipos de culinárias com notas menores.

# 4. Top 3 Insights de dados

    1. A Maior concentração de restaurantes estão localizados na América do Norte, Europa e Ásia.
    2. O maior Preço médio de um prato para duas pessoas pode chegar à mais de 130.000 em moeda local
    3. Na base de dados, mesmo tendo mais de 7500 linhas, existem apenas apenas 2 restaurantes com a modalidade "Home-made"

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: https://mlmauriciolopes-fome-zero-project.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Da visão da Empresa, podemos concluir que o número de pedidos cresceu entre a semana 06 e a semana 13 do ano de 2022.

# 7. Próximo passos

   1. Reduzir o número de métricas.
   2. Criar novos filtros.
   3. Adicionar novas visões de negócio.
