import os
print("Ejercicio 3")
ausente=0
contA=0
contB=0
contC=0
porcB=0
porcC=0
contTrabajadores=0
horasExtrasTrabajadas=int(input("Ingrese la cantidad de horas trabajadas "))
while horasExtrasTrabajadas>=0:
    contTrabajadores+=1
    ausente=int(input("Ingrese cuantos días se ausentó "))
    while ausente<0:
        ausente=int(input("Ingrese cantidad de días ausentado válido! "))
    if ausente==0:
        contA+=1
    if horasExtrasTrabajadas>=10:
        contB+=1
    if horasExtrasTrabajadas>=5 and ausente<3:
        contC+=1
    horasExtrasTrabajadas=int(input("Ingrese la cantidad de horas trabajadas "))
if contTrabajadores>0:
    porcB=(contB*100)/contTrabajadores
    porcC=(contC*100)/contTrabajadores
#A
    print("La cantidad de trabajadores que no faltaron, fue de",contA,"trabajadores")
#B
    print("El porcentaje de trabajadores que trabajaron 10 horas extras o más, fue del "+str(porcB)+"%")
#C
    print("El porcentaje de trabajadores que trabajaron 5 horas extras o más y faltaron menos de 3 días, fue del "+str(porcC)+"%")
else:
    print("¡No se ingresaron trabajadores!")
input("\033[1mPresione enter para salir\033[0m")
os.system('cls')