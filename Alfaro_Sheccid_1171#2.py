print("")
print("Alfaro_Ibarra_Sheccid_3w_1171")
#Definir y preguntar al usuario
print("Programa que coloque numeros del mayor a menos que el usuario pide.")
a=(input("Incerte el primer numero:"))
b=(input("Incerte el segundo numero:"))
c=(input("incerte el tercer numero:"))
#Utilizar if para ordenar los numeros  que ha colocado el usuario
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