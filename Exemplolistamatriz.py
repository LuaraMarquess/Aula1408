print ("Eis, o teclado númerico do terminal: ")
teclado = [["1","2","3"],
           ["4","5","6"],
           ["7","8","9"],
           ["*","0","#"]]

senha = []
print("Digite a senha de 4 digitios....")
for x in range(0,4):
    #senha.append(int(input(f'Digite o digito {x+1}:')))
    senha.append(input(f'Digite o digito {x+1}:'))
for x in range(0,4):
    for y in range(0,3):
        for z in range(0,4):
            if teclado[x] [y] == senha[z]:
                teclado[x][y] = "X"
print("Eis, a senha digitada: ", senha)
print("Confira, as teclas acionadas: ")
for lista in teclado:
    print(lista)
            