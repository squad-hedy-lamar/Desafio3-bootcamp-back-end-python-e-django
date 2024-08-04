"""

6. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre-se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

"""
nome = list(input("Digite seu nome: ").upper())
nome.reverse()
print("O nome ao contrario é: ",end="")
for k in nome:
    print(k,end = "")

