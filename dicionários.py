#dicionário se cria com chaves{}

dados = {"vinissdiaz@gmail.com":{"nome": "Vinicius", "idade": 28, "telefone":"3333-1234"},
         "vinissdiaz15@gmail.com":{"nome": "Leonardo", "idade": 35, "telefone":"9939-1234"},
         "vinissdiaz@hotmail.com":{"nome": "Marcos", "idade": 20, "telefone":"6436-2134"}
         }

telefone = dados["vinissdiaz@hotmail.com"]["telefone"]

print(telefone)

extra = dados["vinissdiaz15@gmail.com"]
print(extra,"\n")

#Percorre o dicionário
for i, valor in dados.items():
    print(i, valor)

print("")
#clear: exclui os elementos
"""dados.clear()
print("Clear:",dados)
"""
#fromkeys: para adicionar novos elementos no dicionário
dados.fromkeys(["nome", "telefone"],"David")
print(dados,"\n")

#get: verifique se existe o elemento
chave = dados.get("chave", {})
print("Chave: ",chave)
busca = dados.get("vinissdiaz15@gmail.com", {})
print("Busca: ",busca,"\n")

#keys
chave = dados.keys()
print("Busca Chaves: ",chave,"\n")

#del: remove elementos especificos
del dados["vinissdiaz15@gmail.com"]

for i, valor in dados.items():
    print(i, valor)

print("")


#update
dados.update({"vinissdiaz@gmail.com": {"nome": "David", "telefone": "1689-1864"}})
print(dados)
