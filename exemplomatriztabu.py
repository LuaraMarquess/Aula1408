print ("Eis, a tabela númerica original ")
tabuada = [[1,2,3],
           [4,5,6],
           [7,8,9]]
multiplicar = int(input("Digite o multiplicador: "))

for x in range(0,3):
    for y in range(0,3):
        tabuada[x][y] = tabuada [x][y] * multiplicar
print("Eis,o multiplicador: ",multiplicar)
print("Confira o resultado  das operações")

for resultado in tabuada:
    print(resultado)