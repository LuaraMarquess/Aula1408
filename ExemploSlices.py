#Demonstração de acesso a listas...
#SLICES 

print("Vou montar a marmmita com 5 elementos! ")
marmmita = ["feijão","arroz","legumes","salada","carne"]
print("Eis, a nossa recomendação: ",marmmita)
resposta = input("Você quer montar uma marmita diferente: (S/N)? ")
if resposta =="S":
    for x in range(0,5):
        print(f'Digite o {x+1} o item do cardápio: ')
        marmmita[x] = input()
        print("A marmita montada foi: ",marmmita)
        print("O três primeiros itens foram: ",marmmita[0:3])
        print("O último item da marmita foi: ", marmmita[-1])
else:
    print("Ok, você decide...")

    #PEP 8
#COLOCO "," + ENTER
#del funcao