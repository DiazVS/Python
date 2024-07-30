saldo = 0
opcao = -1
print("""
    ====================================
                Conta Bancaria
    ====================================
      """)
while opcao != 0:
    opcao = int(input("Selecione uma das opções:\n[1] Depositar\n[2] Saque\n[3] Extrato\n"))

    if opcao == 1:
        valor = int(input("Valor Depositado: "))
        saldo += valor
        print("Novo saldo:", saldo)
    
    elif opcao == 2:
        valor = int(input("Valor para Saque: "))

        if valor <= saldo:
            saldo -= valor
            print("Novo saldo:", saldo)

        else:
            print("Saldo insuficiente para o saque.")
    
    elif opcao == 3:
        print("Saldo Atual:", saldo)
    
    else:
        print("Opção inválida, selecione uma opção válida.")


    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break