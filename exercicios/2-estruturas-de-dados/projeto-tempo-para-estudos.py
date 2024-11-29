# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Qual o seu nome? ')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Qual a quantidade de dias que você estuda por semana? ')
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Horas totais de estudo por semana? ')
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
Curso = input('Qual o seu curso atual? ')
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias = int(total_dias)
total_horas = int(total_horas)

print(f'Olá, {nome}, estudante do {Curso}! De acordo com os dados que você me passou, voce estuda {total_horas/total_dias} horas por dia! meus parabens!!')