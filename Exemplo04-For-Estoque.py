estoque = [100,68,97,45,4]
produtos = ["coca cola","pepsi","guarana","skol","agua"]
nivel_minimo = 50
for i,qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print (produtos[i],qtde)