#set: retira os elementos duplicados
teste = set([1,2,3,1,3,4])
print(teste)

carros = set(["palio","gol","celta","palio", 2, 1])
print(carros)

#Union: full join igual o SQL
full = teste.union(carros)
print("Full Join: ",full)

#intersection: inner join igual o SQL
inner = teste.intersection(carros)
print("inner join: ",inner)

#difference: right join igual o SQL
right = teste.difference(carros)
print("right join: ",right)

#symmetric_difference: full outer join, traz tudo que não tem igual uma da outra igual o SQL
fullouter = teste.symmetric_difference(carros)
print("Full Outer : ",fullouter )

#Add: adiocna novo elemento

vendas = {1, 2000}

vendas.add(16)
vendas.add(25)
vendas.add(16)
print("Add:",vendas)

#discard: igual o remove, porém se o elemento não existir ele ignora
vendas.discard(2000)
vendas.discard(0)
print("discard:",vendas)
