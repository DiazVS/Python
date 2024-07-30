palavra = str(input("Informe a palavra: "))
print (palavra.upper())
print (palavra.lower())
print (palavra.title())

#Remover Espaço em Branco no campo
print (palavra.strip())

#Junções
print(".".join(palavra))

#f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")

#Fatiamento
nome = str(input("Informe o nome: "))
print(nome[:8])
print(nome[9:])
print(nome[::-1])

print("""
    ====================================
                Conta Bancaria
    ====================================
      """)