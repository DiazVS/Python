print("First Code in VScode")

print(5 * 10 + 6)

print(True)

limite = 200
saldo = 1000

while True:
    try:
        saque = float(input("Digite o valor a sacar (ou '0' para sair): "))
        if saque == 0:
            print("Saindo...")
            break
        elif saque > limite:
            print("Erro: Saque maior que o limite disponível.")
        else:
            saldo -= saque
            print(f"Saque realizado. Novo saldo: {saldo}")
    except ValueError:
        print("Erro: Valor inválido. Digite um número válido.")
