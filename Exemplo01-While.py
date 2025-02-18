print ("Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada")
venda = input("Registre um produto : ")
vendas = []
#Crie aqui o programa
while venda != "":
    vendas.append(venda)
    print ("")
    print ("Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada")
    venda = input("Registre um produto : ")
print ("")
print ("REGISTROS FINALIZADO . As vendas cadastradas foram : {}".format(vendas))