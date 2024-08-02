'''
3. Crie um dicionário representando um carrinho de compras. Adicione produtos (chaves) e quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.
'''
precos = {
    "maça": 0.5,
    "banana": 0.3,
    "laranja": 0.4,
    "pão": 1.0,
    "leite": 1.5
}

carrinho = {
    "maça": 4,
    "banana": 10,
    "laranja": 5,
    "pão": 2,
    "leite": 3
}

total = 0.0
for produto, quantidade in carrinho.items():
  if produto in precos:
    total += quantidade * precos[produto]

print(f"Total do carrinho de compras: R${total:.2f}")