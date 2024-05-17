import sys

print("Lista 1:")

lista11 = input("Digite o 1º número da lista 1: ") #Recebe o input do nº 1 número da lista 1
lista21 = input("Digite o 2º número da lista 1: ") #Recebe o input do nº 2 número da lista 1
lista31 = input("Digite o 3º número da lista 1: ") #Recebe o input do nº 3 número da lista 1
lista41 = input("Digite o 4º número da lista 1: ") #Recebe o input do nº 4 número da lista 1

lista1 = [lista11, lista21, lista31, lista41] #Define a lista 1 como uma lista de todos os números

print("Agora a lista Nº2")

lista12 = input("Digite o 1º número da lista 2: ") #Recebe o input do nº 1 número da lista 2
lista22 = input("Digite o 2º número da lista 2: ") #Recebe o input do nº 2 número da lista 2
lista32 = input("Digite o 3º número da lista 2: ") #Recebe o input do nº 3 número da lista 2
lista42 = input("Digite o 4º número da lista 2: ") #Recebe o input do nº 4 número da lista 2

lista2 = [lista12, lista22, lista32, lista42] #Define a lista 2 como uma lista de todos os números

print("Agora a lista Nº3")

lista13 = input("Digite o 1º número da lista 3: ") #Recebe o input do nº 1 número da lista 3
lista23 = input("Digite o 2º número da lista 3: ") #Recebe o input do nº 2 número da lista 3
lista33 = input("Digite o 3º número da lista 3: ") #Recebe o input do nº 3 número da lista 3
lista43 = input("Digite o 4º número da lista 3: ") #Recebe o input do nº 4 número da lista 3

lista3 = [lista13, lista23, lista33, lista43] #Define a lista 3 como uma lista de todos os números

i = 0 #Define o contador de listas em que existe uma órdem crescente

if lista1[0] <= lista1[1] and lista1[1] <= lista1[2] and lista1[2] <= lista1[3] : #Verifica se está em ordem crescente
    i = i + 1 #Caso esteja em ordem crescente adiciona 1 ao contador

if lista2[0] <= lista2[1] and lista2[1] <= lista2[2] and lista2[2] <= lista2[3] : #Verifica se está em ordem crescente
    i = i + 1 #Caso esteja em ordem crescente adiciona 1 ao contador

if lista3[0] <= lista3[1] and lista3[1] <= lista3[2] and lista3[2] <= lista3[3] : #Verifica se está em ordem crescente
    i = i + 1 #Caso esteja em ordem crescente adiciona 1 ao contador

print(i) #Da como saida o contador de listas em órdem crescente

exit()




