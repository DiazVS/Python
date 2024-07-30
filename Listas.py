Comidas = ["Pizza", "Esfiha", "Pastel"]
print(Comidas)

m = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]
print(m)

#Filtros
#append: adiciona novo elemento na lista
#extend: junta com outros elementos
n = [1,30,21,2,9,65,34]
pares = []

for numeros in n:
    if numeros % 2 == 0:
        pares.append(numeros)
print("\nPares: ",pares)


print("\nExtend:")
lin = ['R','C']

print(lin)

lin.extend(['java', 'C#'])

print(lin)

#sort: ordena lista
print("\nSort: ")
lin.sort()

print(lin)

#remove: remove elemento da lista
print("\nRemove: ")
lin.remove("C")

print(lin)