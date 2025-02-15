nomes = ["enzo", "marcos", "lucas", "gustavo", "vitor"]
tel = ["47 9465-2732", "47 9854-8736", "47 9371-2245", "47 9826-4122", "47 8647-2841"]
endereco = ["comasa", "jardim paraiso", "aventureiro", "boa vista", "itau"]
produto = input("Insira o nome da pessoa : ")
if produto in [nomes]:
    i = nomes.index(produto)
    tel1 = tel[i]
    endereco1 = endereco[i]
    print ("nome : {} e o telefone : {} mora do bairro :{}".format(nome1, tel1, endereco1 ))
else:
    print("{} não existe esse nome no sistema".format(produto))
