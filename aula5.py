lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo' , "arara"] # na lista se na posição 0 eu querer colocar o macaco
#lista_animal(0) = 'macaco'. na tupla ão da para alterar um objeto dela.
tupla = (1, 10, 12, 14) # tupla não sofre alterações.
print(len(tupla))
print(len(lista_animal)) #retorna quantos elementos tem na tupla ou na lista.
tupla_animal =  tuple(lista_animal) #para converter lista para tupla.
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
 #para criar lista [], para criar tupla()
#
# #print(lista_animal[1])
# lista.sort() #sort é para ordehttps://
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse() #reverse para reverter a lista de tras para frente.
# print(lista_animal)
# # soma = 0
# # x: int
# # for x in lista:
# #     print(x)
# #     soma += x
# print(sum(lista))  # sum é igual a soma.
# print(max(lista))  # max é igual ao maior numero da lista.
# print(min(lista))  # min é igual ao menor valor.
# print(min(lista_animal))  # funciona para strging.
#
# if 'gato' in lista_animal:  # para saber se existe gato dentro da lista.
#     print('Existe gato na lista. ')
# else:
#     print('Não existe um gato na lista. ')
# lista_animal.append('lobo')  # .append,  para incluir novos nomes a lista.
# print(lista_animal)
# lista_animal.pop(5) #pop retira da lista, ou ultilizar o remove.
# print(lista_animal)
