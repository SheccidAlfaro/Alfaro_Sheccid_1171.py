print("")
print("Alfaro_Ibarra_Sheccid_3w_1171")
#se define y se requiere poner dos numeros que el usuario introduzca
print("Escribe dos numeros para saber cual es el mayor y el menor, suma tambien. :)")
num1=(input("Coloca el primer numero:"))
num2=(input("Coloca el segundo numero:"))
#Se utiliza if para saber el numero menor y menor
if num1 > num2:
    print(" el primer numero es mayor y el numero dos es el menor.")
elif num2 >num1:
    print ("el segundo numero es mayor y el numero uno es el menor.")
#Se define la variable que sume los numeros
sm=num1+num2
#Se muestra en pantallla el resultado
print("La suma de los numeros es:")
print(sm)