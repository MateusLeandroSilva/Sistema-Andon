# Sistema de Controle de Estoque com Andon

Este projeto implementa um sistema simples de controle de estoque em Python, utilizando o conceito de Andon para indicar visualmente o nível de estoque por meio de mensagens de status.

## Funcionalidades

- Definição do estoque inicial pelo usuário.
- Retirada de peças do estoque.
- Indicação de status do estoque:
  - Luz Verde → Estoque seguro.
  - Luz Amarela → Estoque em atenção (abaixo de 50%).
  - Luz Vermelha → Estoque crítico (abaixo de 15%).
- Aviso de estoque esgotado quando chegar a 0.
- Tratamento de erros para entradas inválidas.

## Como funciona

1. O usuário define o estoque inicial.
2. O sistema calcula os limites de atenção (50%) e crítico (15%).
3. A cada retirada de peças, o saldo do estoque é atualizado.
4. O programa exibe o status do estoque com base nos limites.
5. O programa encerra quando o estoque chega a zero.

## Exemplo de uso
Defina o estoque inicial: 500

Seja Bem-Vindo ao IM-date
Quantidade de peças retiradas: 100
Luz Verde
Peças restantes: 400

Quantidade de peças retiradas: 200
Luz Amarela
Peças restantes: 200

Quantidade de peças retiradas: 190
Luz Vermelha
Peças restantes: 10

Quantidade de peças retiradas: 10
Estoque esgotado!


## Tecnologias utilizadas

- Python 3

## Estrutura do código

- Definição do estoque inicial.
- Cálculo dos limites de atenção (amarelo) e crítico (vermelho).
- Loop principal:
  - Entrada do usuário (quantidade retirada).
  - Atualização do saldo de estoque.
  - Exibição do status.
  - Verificação de esgotamento.

## Possíveis melhorias

- Permitir adição de peças ao estoque.
- Registro de movimentações em arquivo de log.
- Criação de interface gráfica para visualização dos níveis de estoque.


