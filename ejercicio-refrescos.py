#Declaro dos variables para cada uno, correspondientes a los ml y costo de cada refresco
ml_r1=int(input("¿Cuál es la cantidad de ml del primer refresco?: "))
costo_r1=float(input("¿Cuál es el costo del primer refresco?: "))
ml_r2=int(input("¿Cuál es la cantidad de ml del segundo refresco?: "))
costo_r2=float(input("¿Cuál es el costo del segundo refresco?: "))

#Almaceno en dos variables el cálculo de la relación precio/ml de cada refresco
relacion_r1=costo_r1/ml_r1
relacion_r2=costo_r2/ml_r2

#Creo condicionales para comparar la relación precio/ml calculada anteriormente de cada refresco

if(relacion_r1<relacion_r2):
    print("Te ahorras más con el refresco de "+ str(ml_r1))
elif (relacion_r1==relacion_r2):
    print("Ambos te salen por la misma relación precio/ml")
else:
    print("Te ahorras más con el refresco de " + str(ml_r2))
