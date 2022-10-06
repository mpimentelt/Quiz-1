#===================================================
# Nombre del Estudiante: Mariana Pimentel
# Carnet: 20221110154
#===================================================
penta = [[45,78,65],[12,35,70],[51,3,105],[22,12,85]]
for group_numbers in penta:
    for number in group_numbers:
        for n in range(1,number+1):
            aux = (n*(3*(n)-1))/2
            if int(aux) == number:
                print("El número {} es pentagonal.".format(number))
                break
        else:
            print("El número {} no es pentagonal.".format(number))