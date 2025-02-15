lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [11,12,13,14,15]
todas_lista = [lista1, lista2, lista3]
print (todas_lista)

print ("")

produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
print (produtos[1])

print ("")

produtos = ["tv", "celular" , "mouse", "teclado", "tablet"]
vendas = [1000, 1500, 350, 270, 900]
print ("A vendas de {} foram  de {}".format(produtos[1], vendas[1]))

print ("")

produtos = ["tv", "celular", "mouse", "teclado", "tablet"]
i = produtos.index("mouse")
print ("O valor de i é "+ str(i))
print ("O produto da posição i é "+ str(produtos[i]))

print ("")
produtos = ["tv", "celular", "mouse", "teclado", "tablet", "geladeira", "forno"]
estoque = [100,150,100,120,70,180,80]
produto = input("Insira o nome do produto e letra minuscula : ")
if produto in produtos:
    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print ("Temos {} unidade de {} no estoque".format(qtde_estoque, produto))
else:
    print("{} não existe no estoque".format(produto))


