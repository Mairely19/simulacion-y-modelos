#Mairely Rosas 27547288

desde colecciones importar Contador
de importación  aleatoria aleatoria
Importar matplotlib. pyplot como PLT
# Crea una lista vacía para almacenar los valores
datos = []

# Abre el archivo en modo lectura
con open('archivo.csv', 'r') como archivo:
    # Recorre cada línea del archivo
    Para la línea en el archivo:
        # Elimina los caracteres de nueva línea y espacio en blanco
         línea = línea. tira()
        # Agrega el valor a la lista
        datos. append(float(línea))

# Calcula la frecuencia de cada elemento en la lista
frecuencia = Counter(datos)

# Calcula la frecuencia acumulada
frecuencia_acumulada = {}
total = suma(frecuencia. valores())
acumulado = 0
Para clave, valor en frecuencia. artículos():
    acumulado += valor
    frecuencia_acumulada[clave] = acumulado / total

# Crea un diccionario vacío para almacenar los contadores
Contadores = {}

# Itera 100 veces
Para i en rango(100):
    r = aleatorio()
    para clave, valor en frecuencia_acumulada. artículos():
        Si r <= valor:
            # Aumenta el contador para ese valor
            Si tecla en contadores:
                contadores[clave] += 1
            De lo contrario:
                contadores[clave] = 1
            quebrar

# Calcula el porcentaje de que "r" caiga en cada frecuencia acumulada
porcentajes = {}
Para clave, valor en contadores. artículos():
    porcentajes[clave] = (valor / 100) * 100 

# Imprime los datos del archivo
Impresión('-----------------------------------------------------------')
print('Datos')
print(datos)
# Imprime la frecuencia que se repiten los numeros
Impresión('-----------------------------------------------------------')
print('Cantidad de repeticiones:')
print(dict (frecuencia))
# Imprime los porcentajes
Impresión('-----------------------------------------------------------')
print('Porcentaje')
print(porcentajes)
# Imprime la frecuencia acumulada
Impresión('-----------------------------------------------------------')
print('Frecuencia Acumulada')
imprimir(frecuencia_acumulada )

# Crea un gráfico de barras
plt. bar(porcentajes. keys(), porcentajes. valores())

# Agrega títulos al gráfico
plt. title("Simulación de datos")
plt. xlabel("Frecuencia acumulada")
plt. ylabel("Porcentaje")

# Muestra el gráfico
plt. mostrar()
