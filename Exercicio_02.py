# Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
# Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Pergunta sobre o turno de estudo
turno = input('Qual o seu turno? (M-matutino / V-vespertino / N-noturno): ').strip().upper()

# Determina a mensagem a ser impressa com base no turno
if turno == 'M':
    mensagem = "Bom Dia!"
elif turno == 'V':
    mensagem = "Boa Tarde!"
elif turno == 'N':
    mensagem = "Boa Noite!"
else:
    mensagem = "Valor Inválido!"

# Exibe a mensagem final
print(mensagem)
