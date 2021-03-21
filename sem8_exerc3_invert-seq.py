i= 1
lista = []
while (i != 0):
    i = int(input("Digite um número: "))
    lista.append(i)
p = len(lista)
for it in range(p-1):
    print(lista[0-it-2])
