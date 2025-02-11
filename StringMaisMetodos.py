#Transforma apenas a primeira letra de uma string em maiuscupa
nome = "Gustavo"
print (nome.capitalize(),"\n")

#Transforma todas as letras em minuscula
nome = "GUSTAVO"
print (nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING.
nome = "GustavoSousa"
print (nome.count ("s") , "\n")

#RETORNA true (verdadeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPECIFICA
nome = "GustavoSousa"
print(nome.endswith("gmail.com"),"\n")

#ENCONTRA A POSIÇÃO DO TERMO PROCURADO.
#LEMBRE=SE COMEÇA DO zero
nome = "GustavoSousa@gmail.com"
print (nome.find ("@"), "\n")

#VERIFICA SE O TESTO É TODO FEITO COM LETRA
nome = "Gustavo"
print(nome.isalpha(),"\n")

#VERIFICA SE O TESTO É FEITO COM NUMEROS
nome = "123"
print (nome.isnumeric(),"\n")

#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO
nome = "justavo"
print (nome.replace("o"),("0"),"\n" )

#SEPARA O TEXTO STRING BASEADO EM ALGUM CARACTERE INDICADO
nome = "Gustavo @ Max"
print(nome.split("@"),"\n")

#COLOCAR TODAS AS LETRAS INICIAUS EM MAIUSCULA
nome = "gustavo dos santos de sousa"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDESEJADOS , COMO POR EXEMPLO espaços QUE NÃO AGREGAM VALOR.
nome = " Gustavo Dos Santos De Sousa"
print(nome.strip(),"\n")

#RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO
nome = "Gustavo 2008"
print(nome.startswith("ser"), "\n")
print(nome.startswith("ser"), "\n")

