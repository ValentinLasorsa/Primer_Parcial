import os
print("Ejercicio 1")
num1=float(input("Ingrese el primer número "))
num2=float(input("Ingrese el segundo número "))
if num1>num2:
    print("Se encuentran en orden decreciente")
else:
    print("Se encuentran en orden creciente")
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')