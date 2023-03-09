#!/user/bin/env python3
# Mairely Rosas 27547288

import estadisticas como st
import csv 
import matplotlib . pyplot como plt

def descriptiva_datos ( archivo ):
    con abierto ( archivo , ´r´) como f:

        lista = []
        altura = []
        lector = csv . lector (f)

        #Continuamos con (lector, ninguno)
        
        for fila en lector:
            lista _ agregar ( lista ( mapa (float , fila)))

        for x en lista:
            alturas += x

        #procedemos a imprimir los datos:
        imprimir ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ ")
        print (f"Datos: { alturas }")
        imprimir ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ ")
        alturas . ordenar ()
        print (f"1. Ordenar los datos (de menor a mayor): {altura} ")
        imprimir ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ ")
        print (f"2. Medidas de tendencia cental")
        medios = calle . media (alturas) #aqui representamos la media
        print (f"La media es: {media}")
        moda = st . modo (alturas) #aqui representamos la moda
        print (f"La mediana es: {moda}")
        mediana = st . mediana (alturas) #aqui representamos la mediana
        print (f"La moda es: {moda}")
        imprimir ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ ")
        print ("3. Medidas de dispersion:")
        varianza = st . varianza (alturas) #aqui representamos la varianza
        print (f"La varianza es: {varianza}")
        des_est = calle . stdev (altura) #Desviacion estandar
        print (f"La desviacion estandar es: {des_est}")
        rango = alturas [ len (alturas) - 1] - alturas [0] #representacion del rango
        print (f"El rango es: {rango}")
        imprimir ("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ ")

        #Procedemos a realizar las graficas en matpotlib

        por favor hist (alturas , bins = [1.3 , 1.35 , 1.4 , 1.45 , 1.5 , 1.55 , 1.6 , 1.65 , 1.7 , 1.75 , 1.8 , 1.9 , 2], edgecolor = ´black´)
        por favor xlabel ( ´Estaturas´ )
        por favor ylabel ( ´Veces que se repite´ )
        por favor title ( ´ Histograma de las estaturas´ )
        por favor mostrar ()

if __nombre__ == "__principal__":
       archivo = ´datos1.csv´
       descriptiva_datos (archivo)