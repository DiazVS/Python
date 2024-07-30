# Lista para armazenar os itens
itens = []

#TODO: Solicite os itens ao usuário
item1 = input("Item1: ")
item2 = input("Item2: ")
item3 = input("Item3: ")
itens = [item1, item2, item3]
# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")