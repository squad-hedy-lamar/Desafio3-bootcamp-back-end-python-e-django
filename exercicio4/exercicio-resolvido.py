# Exercicio 4 - Crie um dicionário representando contatos (nome, telefone). Permita ao usuário procurar por um contato pelo nome.


# Definição do dicionário
dicionario_contatos = {
    "João": "03398147-1234",
    "Tereza": "07098245-6565",
    "Elisa": "02194562-4565",
    "Felipe": "0313245-8987",
    "Maria": "04597895-6520",
    "Lauro": "05199999-8585"
}


# Criação de função para procurar contato pelo nome
def procurar_contato(nome):
    nome = nome.lower()

# lista de apoio para desconsiderar diferença de letra minuscula
    contatos_minuscula = {k.lower(): v for k, v in dicionario_contatos.items()}

    telefone = contatos_minuscula.get(nome)

    if (telefone):
# Buscando o nome registrado
        nome_inicial = next(k for k, v in dicionario_contatos.items() if k.lower() == nome)
        return(f"{nome}: {telefone}")
    else:
        return("O contato não foi encontrado!")

# Solicitando usuário para digitar o contato para busca
nome = str(input("Digite o nome do contato a ser procurado: "))
retorno = procurar_contato(nome)
print(retorno)
