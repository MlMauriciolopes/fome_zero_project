# 1. Problema de negócio

A Fome Zero! é uma empresa de tecnologia que criou um aplicativo que conecta restaurantes, entregadores e pessoas.

Através desse aplicativo, você consegue ter uma vasta visão de, como andam o gerenciamento, as classificações, e os melhores lugares para visitar lugares gastronômicos, com um simples toque de botão.

Outra vantangem é que, você pode ter uma boa ideia da cultura local e das avaliações, sem sair de casa, e/ou ir preparado para uma escolha mais acertiva de escolha.

Você foi contratado como um Cientista de Dados para criar soluções de dados para entrega, mas antes de treinar algoritmos, a necessidade da empresa é ter um os principais KPIs estratégicos organizados em uma única ferramenta, para que o CEO possa consultar e conseguir tomar decisões simples, porém importantes.

A Fome Zero! possui um modelo de negócio chamado Marketplace, que fazer o intermédio do negócio entre três clientes principais: Cidades, Países e tipos de culinárias. Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:
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

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 2. Premissas assumidas para a análise

    1. A análise foi realizada com dados entre 11/02/2022 e 06/04/2022.
    2. Marketplace foi o modelo de negócio assumido.
    3. Os 3 principais visões do negócio foram: Visão transação de pedidos, visão restaurante e visão entregadores.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:

    1. Visão do crescimento da empresa
    2. Visão do crescimento dos restaurantes
    3. Visão do crescimento dos entregadores

Cada visão é representada pelo seguinte conjunto de métricas.

    Visão do crescimento da empresa
       1. Pedidos por dia
       2. Porcentagem de pedidos por condições de trânsito
       3. Quantidade de pedidos por tipo e por cidade.
       4. Pedidos por semana
       5. Quantidade de pedidos por tipo de entrega
       6. Quantidade de pedidos por condições de trânsito e tipo de cidade

    Visão do crescimento dos restaurantes
       1. Quantidade de pedidos únicos.
       2. Distância média percorrida.
       3. Tempo médio de entrega durante festival e dias normais.
       4. Desvio padrão do tempo de entrega durante festivais e dias normais.
       5. Tempo de entrega médio por cidade.
       6. Distribuição do tempo médio de entrega por cidade.
       7. Tempo médio de entrega por tipo de pedido.

    Visão do crescimento dos entregadores
       1. Idade do entregador mais velho e do mais novo.
       2. Avaliação do melhor e do pior veículo.
       3. Avaliação média por entregador.
       4. Avaliação média por condições de trânsito.
       5. Avaliação média por condições climáticas.
       6. Tempo médido do entregador mais rápido.
       7. Tempo médio do entregador mais rápido por cidade.

# 4. Top 3 Insights de dados

    1. A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximadamente 10% do número de pedidos em dia sequenciais.
    2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.
    3. As maiores variações no tempo de entrega, acontecem durante o clima ensoladao.

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
