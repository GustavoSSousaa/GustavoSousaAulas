pessoas_presentes = ["carlos", "sapeca", "goku","calabreso"]
chamada = "sapeca"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print ("{} está presente." .format(chamada))
        break
    else:
        print ("Só um print para mostrar que o for passou por essa pessoa : "+str(pessoa))

print ("")
pessoas_presentes = ["carlos", "sapeca", "goku","calabreso"]
chamada = "sapeca"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print ("{} está presente." .format(chamada))
        break
    else:
        print ("Só um print para mostrar que o for passou por essa pessoa : "+str(pessoa))
        continue