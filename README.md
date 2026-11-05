# Exercício Prático — Mock Object (`CustomStack` & `NumberAscOrder`)

Projeto desenvolvido em Python aplicando **TDD**, **Testes de Unidade** e **Mock Objects** com `pytest`, `pytest-cov` e `pytest-mock`, atingindo **100% de cobertura de código**.

## Estrutura do Projeto

```text
├── src/
│   ├── custom_stack_class.py   # Implementação de CustomStack, StackEmptyException e StackFullException
│   └── number_asc_order.py     # Implementação de NumberAscOrder.sort()
├── test/
│   ├── custom_stack_test.py    # Testes de unidade da CustomStack (100% de cobertura)
│   └── number_asc_order_test.py# Testes de unidade da NumberAscOrder utilizando Mock Objects
└── requirements.txt            # Dependências do projeto
```

## Instalação das Dependências

```sh
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Execução dos Testes e Cobertura

```sh
pytest -v --cov=src --cov-report=term-missing
```

## Escopo dos Testes

- **Parte 1 (`CustomStack`)**:
  - Inserção de elementos (`push`) dentro do limite e validação de `size()`, `top()` e `is_empty()`.
  - Lançamento de `StackFullException` ao exceder a capacidade máxima.
  - Remoção de elementos (`pop`) validando o retorno do topo e decremento de tamanho.
  - Lançamento de `StackEmptyException` ao executar `pop()` ou `top()` em uma pilha vazia.
- **Parte 2 (`NumberAscOrder` com Mock Object)**:
  - Ordenação ascendente de uma pilha mockada com 6 dezenas sorteadas aleatoriamente.
  - Retorno de lista vazia `[]` para pilha mockada vazia sem invocar `pop()`.
  - Tratamento de parâmetros inválidos (`None` ou objetos incompatíveis) com lançamento de `TypeError`.
