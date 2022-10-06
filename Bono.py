#===================================================
# Nombre del Estudiante: Mariana Pimentel
# Carnet: 20221110154
#===================================================
number = input("Introduzca un número: ")
isvalid = False
while not number.isnumeric():
    number = input("Introduzca un número: ")
else: 
    number = int(number)
    for i in str(number):
        repeticiones = str(number).count(i)
        if repeticiones == len(str(number)):
            isvalid = True
if isvalid:
    print("El número {} es repunit".format(number))
else:
    print("El número {} no es repunit".format(number))