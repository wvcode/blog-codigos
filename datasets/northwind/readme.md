# Dados Northwind

Um pequeno dataset de vendas de produtos alimenticios gourmet.


| Tabela | Campo | Descrição |
|---|---|---|
| pedidos | pedidoID | Identificador único para cada pedido |
| pedidos | clienteID | O cliente que fez o pedido |
| pedidos | funcionarioID | O funcionário que processou o pedido |
| pedidos | dataPedido | A data em que o pedido foi feito |
| pedidos | dataRequerida | A data em que o cliente solicitou a entrega do pedido |
| pedidos | dataEnvio | A data em que o pedido foi enviado |
| pedidos | transportadoraID | O ID da empresa de transporte utilizada para o pedido |
| pedidos | frete | O custo de envio do pedido (USD) |
| detalhes_pedido | pedidoID | O ID do pedido a que este detalhe pertence |
| detalhes_pedido | produtoID | O ID do produto sendo pedido |
| detalhes_pedido | precoUnitario | O preço por unidade do produto no momento em que o pedido foi feito (USD - desconto não incluído) |
| detalhes_pedido | quantidade | O número de unidades encomendadas |
| detalhes_pedido | desconto | A porcentagem de desconto aplicada ao preço por unidade |
| clientes | clienteID | Identificador único para cada cliente |
| clientes | nomeEmpresa | O nome da empresa do cliente |
| clientes | nomeContato | O nome do contato principal do cliente |
| clientes | tituloContato | O cargo do contato principal do cliente |
| clientes | cidade | A cidade onde o cliente está localizado |
| clientes | pais | O país onde o cliente está localizado |
| produtos | produtoID | Identificador único para cada produto |
| produtos | nomeProduto | O nome do produto |
| produtos | quantidadePorUnidade | A quantidade do produto por embalagem |
| produtos | precoUnitario | O preço atual por unidade do produto (USD) |
| produtos | descontinuado | Indica com um 1 se o produto foi descontinuado |
| produtos | categoriaID | O ID da categoria a que o produto pertence |
| categorias | categoriaID | Identificador único para cada categoria de produto |
| categorias | nomeCategoria | O nome da categoria |
| categorias | descricao | Uma descrição da categoria e de seus produtos |
| funcionarios | funcionarioID | Identificador único para cada funcionário |
| funcionarios | nomeFuncionario | Nome completo do funcionário |
| funcionarios | titulo | O cargo do funcionário |
| funcionarios | cidade | A cidade onde o funcionário trabalha |
| funcionarios | pais | O país onde o funcionário trabalha |
| funcionarios | relatorioPara | O ID do gerente do funcionário |
| transportadoras | transportadoraID | Identificador único para cada transportadora |
| transportadoras | nomeEmpresa | O nome da empresa que fornece serviços de transporte |