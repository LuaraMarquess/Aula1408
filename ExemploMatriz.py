tabuada = []

for x in range(0,10):
    linhas = []
    for y in range(0,10):
        linhas.append(x * y)
    tabuada.append(linhas)

for tabela in tabuada:
    print(tabela)
    