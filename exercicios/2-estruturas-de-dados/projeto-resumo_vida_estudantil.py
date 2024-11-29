# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
pessoa = {}
pessoa['nome'] = input('Olá, qual o seu nome? ')
pessoa['ano_linkedin'] = int(input('Quando conheceu o linkedin? '))
pessoa['ano_atual'] = int(input('Em que ano estamos? '))
pessoa['cursos_realizados'] = input('Quais cursos realizou até agora? \nPor favor separe por ordem cronologica!')
pessoa['cursos_realizados'] = pessoa['cursos_realizados'].split(', ')

print(f"olá, {pessoa['nome']}, você coneceu o LinkedIn no ano {pessoa['ano_linkedin']} e desde lá esta à {int(pessoa['ano_atual']-pessoa['ano_linkedin'])} anos. Até agora você realizou {len(pessoa['cursos_realizados'])} cursos conosco. Seu primeiro curso foi {pessoa['cursos_realizados'][0]} e o último foi {pessoa['cursos_realizados'][-1]}!!")