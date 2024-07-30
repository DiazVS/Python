quantidade_passos = 0

quantidade_passos = int(input("Quantos passos o Explorador terá que dar (digite um número negativo para sair): "))
    
if quantidade_passos > 0:
    for i in range(1, quantidade_passos + 1):
        if i == 1:
            print("Explorador: 1 passo")
        else:
            print("Explorador:", i, "passos")
else:
    print("Nenhum passo dado na floresta.")