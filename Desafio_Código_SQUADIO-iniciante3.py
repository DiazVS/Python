capacidade_atual, aumento_percentual = map(int, input().split())

# TODO: Calcule a nova capacidade do disco de Mithril
calculo = (capacidade_atual * aumento_percentual)/100
nova_capacidade = int(capacidade_atual + calculo)
# TODO: Imprima a nova capacidade
print(nova_capacidade)