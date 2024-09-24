import os
print("Ejercicio 2")
precioU=0
cantVenta=0
codigo=0
precioTotal=0
totalA=0
contB=0
contC=0
porcB=0
promC=0
for u in range(1,6):
    precioU=int(input(f"Ingrese precio unitario del {u} artículo "))
    while precioU<=0:
        precioU=int(input(f"Ingrese precio unitario del {u} artículo COHERENTE "))
    cantVenta=int(input(f"Ingrese la cantidad que desea comprar del {u} artículo "))
    while cantVenta<=0:
        cantVenta=int(input(f"Ingrese la cantidad que desea comprar del {u} artículo COHERENTE "))
    codigo=int(input(f"Ingrese el código de venta del {u} artículo "))
    while codigo<0:
        codigo=int(input(f"Ingrese el código de venta del {u} artículo COHERENTE "))
    precioTotal=precioU*cantVenta
    if codigo >=10 and codigo<=50:
        totalA=totalA+precioTotal
    if precioTotal>15000 or precioTotal<10000:
        contB+=1
    if precioTotal>30000:
        contC+=1
input("\033[1mIngreso finalizado, enter para seguir con los resultados!\033[0m")
porcB=(contB*100)/5
promC=contC/5
#A
print("El total recaudado entre artículos con el código entre 10 y 50 son $"+str(totalA))
#B
print("El porcentaje de ventas que fueron mayores a $15000 o menores a $10000 fue del "+str(porcB)+"%")
#C
print("El promedio de ventas por artículos mayores a $30000 fue de "+str(promC))
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')