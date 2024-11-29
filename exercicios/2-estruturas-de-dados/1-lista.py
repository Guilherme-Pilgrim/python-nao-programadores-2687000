# Crie uma lista apenas com elementos numéricos
idades = [12, 18, 22, 44, 48]
print(idades)
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista_mista = ['string', True, 12, 12.45, 10/3, [1,2,3,4], idades]
print(lista_mista)
# Imprima na tela apenas os 5 primeiros elementos da lista
print(idades)
print(lista_mista[0:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_mista[0:7:2])
# Remova da lista o último item
lista_mista.pop()
print(lista_mista)
# Insira na lista um novo item
idades.append(89)
print(idades)
# Remova da lista um item específico
lista_mista.remove(True)
print(lista_mista)