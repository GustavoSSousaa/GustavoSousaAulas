#Faça um programa que receba uma nota do aluno e se for SUPERIOR ou igual a 7 apareça mensagem que ele esta APROVADO, se for inferior a 5 ele esta NAO APROVADO/REPROVADO DiRETO
#e se estiver entre 5 e 7 apareça a mensagem NAO APROVADO/RECUPEAÇÂO
n1 = int(input("Digite sua nota : "))

if(n1 >= 7):
    print("Voce esta APROVADO")
else:
    if(n1 >= 5):
        print("Voce esta em RECUPERAÇÂO")
    else:
        print("Voce esta REPROVADO (SEU BURRO 🤦‍♂️)") 