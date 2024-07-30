def exibi_msg(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!\n")

exibi_msg()
exibi_msg(nome = "Vinicius")



#Argumento nomeado
def salvar_carro(marca1,modelo,ano,placa):
    print(f"Carro Inserido com sucesso!\n-{marca1}/{modelo}/{ano}/{placa}\n")


salvar_carro(marca1="Jeep", modelo="Renegade", ano=2018, placa="OWN-0833")



#Parametros por posição
def cria_carro(modelo,ano,placa, /, marca, motor, combustivel):
    print(f"Carro Inserido com sucesso!\n-{modelo}/{ano}/{placa}/{marca}/{motor}/{combustivel}\n")

#Neste caso a função(def cria_carro(modelo,ano,placa, /, marca, motor, combustivel):), os elementos antes da barra(/) deve estar sem os parametros para funcionar, senão da erro.
cria_carro("Renegade", 2018, "OWN-0833", marca="Jeep", motor="1.6", combustivel="Flex")




#Escopa Global
salario = 3000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

novo_salario = salario_bonus(7000)
print("Salario Novo: ",novo_salario)