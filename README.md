# Alfaro_Sheccid_1171.py
Examen del primer parcial
print("")
print("Alfaro_Ibarra_Sheccid_1171_3w")
#Se definen variables y se pregunta al usuario
nm=(input("Coloca tu nombre:"))
ap=(input("Coloca tu apellido paterno:"))
am=(input("Coloca tu apellido materno:"))
print("")
#Se muestra en pantalla los apellidos y nombres
print(ap)
print(am)
print(nm)

print("")
#Se define variable concatena las demas en un solo parrafo
nc= ap+" "  + am + " " + nm
#Se muestra en pantalla el resultado
print("Bievenido")
print(nc)

print("")
#Utilizar formato de cadena¿?
nt=1171
cr=f"Bienvenido,{nc} {nt}"
#Mostrar en pantalla el resultado
print(cr)

print("")

![image](https://github.com/user-attachments/assets/efeb89a9-f981-45a6-a82e-c431b476aa88)
![image](https://github.com/user-attachments/assets/66ab53fe-b986-47a6-b980-8e7a4a3f3236)
# Programa#2
print("")
print("Alfaro_Ibarra_Sheccid_3w_1171")
#DEfinir variables y preduntar al usuario
print("Programa que coloque numeros del mayor a menos que el usuario pide.")
a=(input("Incerte el primer numero:"))
b=(input("Incerte el segundo numero:"))
c=(input("incerte el tercer numero:"))
#Utilizar if para obtener el orden de numeros
if a==b:
    print("Estas repitiendo valores.")
if a==c:
    print("Estas repitiendo valores.")
if b==c:
    print("Estas repitiendo valores.")

if a>b and b>c:
    print(a,b,c)
if b>a  and a>c:
    print(b,a,c)
if c>a and a>b:
    print(c,a,b)
if a>c and c>b:
    print(a,c,b)
if c>b and b>a:
    print(c, b, a)
if b>c and c>a:
    print(b, c, a)
else:
    print("!")

    ![image](https://github.com/user-attachments/assets/f7e37741-1a16-400b-b40b-5e5e97a9ea2f)
    ![image](https://github.com/user-attachments/assets/0064b6d5-dfce-45f7-a2af-3d125bb8621c)
# Programa#3
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
![image](https://github.com/user-attachments/assets/5799792a-c8e5-4f92-8c37-bbe941431002)
![image](https://github.com/user-attachments/assets/3df85da1-b11e-4415-b1b5-ffcfe74f9386)

# programa #4
print("")
#DEfinir variables y preguntar al usuario
print("Alfaro Ibarra Sheccid 3W 1171 hayar el perimetro y area de un rectangulo")
b1=float(input("Incerta el numero de la base de ancho"))
al=float(input("Incerta la altura"))
#definir variable y hacer operaciones
p=b1 + b1 + al + al
h=b1*al
#Mostrar en pantalla
print("El perimetro es:")
print(p)
print("EL area es:")
print(h)
![image](https://github.com/user-attachments/assets/6b5f2ab3-c9bc-4617-9a2a-d129e11a321a)
![image](https://github.com/user-attachments/assets/1d55e0dd-a699-4dea-9713-f0dc0176c097)

# programa #5
print("")
print("Sheccid Alfaro Ibarra 3w, 11721 numeros naturales")
#SE define y se pregunta al usuario
nmt=int(input("Ingrese un numero natural:"))
#Se utiliza if para saner si es numero natural y si es impar
if nmt <=12:
    print("Esta entre los numeros naturales.")
else:
    print("No esta entre los numeros naturales.")
    
if nmt % 2 == 0 :
    print("es par")#una de las condiciones
#en caso de que la primera opcion sea falsa
else:
    print("es impar")#una de las condiciones

![image](https://github.com/user-attachments/assets/f5a4bbd3-d0d0-4400-b03c-48b8ba64c900)
![image](https://github.com/user-attachments/assets/ac57b677-3ce5-473d-957d-4a772fa8936f)



