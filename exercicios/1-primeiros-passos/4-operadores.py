ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
idade_Gerlaine = ano_formatura - ano_nascimento
print(idade_Gerlaine)

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento <= ano_formatura)
print(21 > idade_Gerlaine)
print(56 == (77 - idade_Gerlaine))

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((24 >= (idade_Gerlaine + 3)) and ('python' == 'gaviao'))