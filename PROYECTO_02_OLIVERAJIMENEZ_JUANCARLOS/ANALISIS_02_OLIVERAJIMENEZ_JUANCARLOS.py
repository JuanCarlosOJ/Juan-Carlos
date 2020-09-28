# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:39:58 2020

@author: karat
"""
import csv

lista_datos = [] #para recopilar los datos del archivo "Documento_exportaciones.csv a manera de lista
with open ("Documento_exportaciones.csv", "r") as archivo:
  lector = csv.reader(archivo)
  for renglon in lector:
    lista_datos.append(renglon) #adicion de los elementos a la lista
# para poder abrir el documento y tener un control de su cierre, con el fin de evitar una saturación de la memoria por un mal manejo o un mal cierre.

# "Consigna 1. Rutas de Importación y Eportación en Synergy Logistics"

#Función para rutas de exportacion e importación

def rutas(dirección): #definición de la función y su argumento
  dirección_contada = []
  conteo_dirección = []
  cuenta = 0
#creación de listas en blanco para recopilar datos y un contador para acumular las veces que se repite un elemento
  for ruta in lista_datos:
      if ruta[1] == dirección:
          ruta_actual = [ruta[2], ruta[3]]
#para poder capturar los elementos de la lista de acuerdo a la condición si el tipo de movimiento (exportación o importación) corresponde a la dirección establecida por la función.
          if ruta_actual not in dirección_contada:
              for movimiento in lista_datos:
                  if movimiento[1] == dirección:
                      if ruta_actual == [movimiento[2], movimiento[3]]:
                          cuenta += 1
# para poder capturar los elementos de la lista, en dado caso de que estos no se encuentren declarados en la primer condición, armado de lista y comprobación de acuerdo a la condición de que la dirección corresponda al tipo de movimiento de cada elemento de la lista, de ser cierta la condición, el contador aumenta un valor por cada vez que se cumpla la condición.                      
              dirección_contada.append(ruta_actual)
              conteo_dirección.append([ruta[2], ruta[3], cuenta])
              cuenta = 0
# armado de las primeras listas en blanco predefinidas y reinicio del contador para poder contar un segundo elemento correspondiente de la lista.
  return conteo_dirección # para reiniciar la función y no tener una sobreescritura de documentos.

# "Consigna 2. Medios de transporte utilizados por Synergy Logistics"
#creación de una lista de forma manual donde se capturaron los elementos que corresponden a la vía de transporte utilizada independiente al tipo de movimiento realizado por la empresa, el contador_transportes será utilizado para contabilizar las veces que un medio de transporte definido sea utilizado y la lista_medios_transporte recopilará las veces que se utiliza cada medio de transporte, a fin de mostrar la información obtenida más adelante.
medios_de_transporte = ['Air', 'Rail', 'Road', 'Sea']
contador_transportes = 0
lista_medios_transporte = []
#las iteraciones y condicionales siguientes serán de ayuda para poder determinar las veces que un medio de transporte sea utilizado, así contador_transportes aumenta un valor por cada vez que se utiliza dicho medio.
for medio in medios_de_transporte:
  for transporte in lista_datos:
    if transporte[7] == medio:
      contador_transportes += 1
#una plantilla creará una lista que contiene al medio de transporte utilizado y las veces que este sea utilizado, al finalizar, serán añadidos a la lista_medios_transporte, por ultimo, se reinicia el contador_transportes para contabilizar un medio de transporte distinto.
  plantilla = [medio, contador_transportes]
  lista_medios_transporte.append(plantilla)
  contador_transportes = 0
lista_medios_transporte_ordenada = sorted(lista_medios_transporte, key = lambda x: x[1]) #función para ordenar las veces que se utiliza un medio de transporte en orden ascendente (de menor a mayor)

#"Consigna 3. Países que generan ingresos en exportaciones e importaciones"
#a diferencia de la consigna 1, no consideré elaborar una función para esta consigna, debido a que para los países que llevan a cabo exportaciones se toma en cuenta el origen, representando al país que lleva a cabo el envío (exportación) mientras que a los países que llevan a cabo importaciones se toma en cuenta el destino considerando este como el país del cual viene la importación ya que origen es el país que recibe dicho movimiento.
#para comenzar se eliminó el encabezado de la lista_datos debido a que este solo representa las variables y la estructura de la lista, un calculador servirá para capturar los ingresos recibidos por cada país, la iteración aumenta según el total de ingresos obtenidos por cada movimiento realizado para así obtener el total de dinero reunido por todos los movimientos realizados.

#Calculo de ingresos totales (exportaciones e importaciones)
lista_datos.pop(0)
calculador = 0
for dinero in lista_datos:
  calculador += int(dinero[9])

#Exportaciones
dirección = "Exports"
exportaciones_cuenta = 0
exportaciones_ingresos = 0
contadas_exportaciones = []
exportaciones_conteo = []

for exportación in lista_datos:
    if exportación[1] == dirección:
        remitente = [exportación[2]]
        
        if remitente not in contadas_exportaciones:
            for movimiento in lista_datos:
                if movimiento[1] == dirección:
                    if remitente == [movimiento[2]]:
                        exportaciones_cuenta += 1
                        exportaciones_ingresos += int(movimiento[9])
                    
            contadas_exportaciones.append(remitente)
            exportaciones_conteo.append([exportación[2], exportaciones_cuenta, exportaciones_ingresos])
            exportaciones_cuenta = 0
            exportaciones_ingresos = 0

total_exportaciones = 0
for elemento in exportaciones_conteo:
  total_exportaciones += elemento[2]

lista_exportaciones_porcentaje = []
for export_pais in exportaciones_conteo:
  porcentaje_export = ((export_pais[2]/total_exportaciones)*100)
  lista_exportaciones_porcentaje.append([export_pais[0], export_pais[1], export_pais[2], porcentaje_export])

lista_exportaciones_porcentaje_ordenada = sorted(lista_exportaciones_porcentaje, key = lambda x: x[3])
lista_exportaciones_ordenada = reversed(lista_exportaciones_porcentaje_ordenada)

#Importaciones
dirección = "Imports"
importaciones_cuenta = 0
importaciones_ingresos = 0
contadas_importaciones = []
importaciones_conteo = []

for exportación in lista_datos:
    if exportación[1] == dirección:
        remitente = [exportación[3]]
        
        if remitente not in contadas_importaciones:
            for movimiento in lista_datos:
                if movimiento[1] == dirección:
                    if remitente == [movimiento[3]]:
                        importaciones_cuenta += 1
                        importaciones_ingresos += int(movimiento[9])
                    
            contadas_importaciones.append(remitente)
            importaciones_conteo.append([exportación[3], importaciones_cuenta, importaciones_ingresos])
            importaciones_cuenta = 0
            importaciones_ingresos = 0

total_importaciones = 0
for elemento in importaciones_conteo:
  total_importaciones += elemento[2]

lista_importaciones_porcentaje = []
for import_pais in importaciones_conteo:
  porcentaje_import = ((import_pais[2]/total_importaciones)*100)
  lista_importaciones_porcentaje.append([import_pais[0], import_pais[1], import_pais[2], porcentaje_import])

lista_importaciones_porcentaje_ordenada = sorted(lista_importaciones_porcentaje, key = lambda x: x[3])
lista_importaciones_ordenada = reversed(lista_importaciones_porcentaje_ordenada)

#para lasimportaciones e importaciones, se comenzó por definir el tipo de dirección de modo manual y establecer contadores para las veces que se repite un país y el total de ingresos que este genera por cada vez que importa o exporta, según sea el caso, y dos listas, para capturar los países que se mencionan y sus ingresos. Una iteración ayudará a acceder a cada elemento de la lista y un condicional establece cual movimiento corresponde a importación o exportación, se ser correspondiente cada caso, se elabora una variable que corresponde al remitente que representa al país que importa o exporta, de no encontrarse el remitente en una lista, se establece un nuevo condicional a partir de una segunda iteración para acceder a los elementos de la lista y establecer nuevamente la condición de que tipo de movimiento se realiza, si este corresponde a la dirección correspondiente se comprueba que el remitente corresponda al país que realiza la importación, de ser ciertas estas condiciones, el contador  aumenta 1 valor por cada vez que se menciona el país y un segundo contador aumenta según el valor del ingreso de este movimiento, después se construye una lista con el país, las veces que se menciona y el total de ingresos que genera.
#para poder manejar los porcentajes relativos de cada ingreso de cada país, se estableció un contador para llevar la cuenta del total de importaciones o exportaciones, después se armó una lista para concentrar la información de cada país y sus ingresos, una iteración nos permite acceder a cada elemento de la lista, luego se obtiene el porcentaje relativo dividiendo el ingreso que genera el país entre el total de ingresos por importación o exportación y multiplicando este resultado por 100, después se contruye la lista concentrando el país, las veces que se menciona en cada movimiento, el total de ingresos que genera y el porcentaje relativo de estos ingresos, por último se ordenan las listas de modo descendente (de mayor porcentaje de ingreso a menor porcentaje de ingreso)

print('Bienvenido al portal de "Synergy Logistics", ¡donde nuestros productos se envían por todo el mundo para generar sonrisas y comodidades! \n¿Qué desea hacer hoy?')
#mensaje de bienvenida

#Menú
#para poder acceder a cada una de las operaciones realizadas anteriormente, según sea lo que se quiera visualizar, se encuentran un total de 6 opciones, por medio de un input se puede acceder a ellas colocando en opción el numero que corresponde según el menú de opciones, mientras estos numeros se mencionen y sean menores que 6, serán mostrados cuantas veces se desean.
opcion = 0
while opcion != '6':

  pregunta = '\nPara seleccionar una opción, por favor escriba el número de la opción y pulse Enter\n 1. Ver las 10 rutas de exportación más demandadas.\n 2. Ver las 10 rutas de importación más demandadas.\n 3. Ver el listado del total de medios de transporte utilizados para realizar exportaciones e importaciones de la empresa.\n 4. Ver los países que generan ingresos de exportaciones en Synergy Logistics.\n 5. Ver los países que generan ingresos de importaciones en Synergy Logistics.\n 6. Salir'
  print(pregunta)
  opcion = input('Opción: ')

  if opcion == '1':
    lista = rutas('Exports')
    print('Estas son las rutas de exportación de Synergy Logistics')
    print('Formato de lista: [pais origen, pais destino, conteo de ruta]')
    for ruta in reversed(sorted(lista, key = lambda x: x[2])):
      print(ruta)
  elif opcion == '2':
    lista = rutas('Imports')
    print('Estas son las rutas de importación de Synergy Logistics')
    print('Formato de lista: [pais origen, pais destino, conteo de ruta]')
    for ruta in reversed(sorted(lista, key = lambda x: x[2])):
      print(ruta)
  elif opcion == '3':
    print('Aquí las vías de transporte usadas por Synergy Logistics:')
    print('Formato de lista: [vía de transporte, veces utilizada]')
    for medio_transporte in reversed(lista_medios_transporte_ordenada):
      print(medio_transporte)
  elif opcion == '4':
    print('El total de ingresos por exportaciones por Synergy Logistics fue de', total_exportaciones, 'unidades')
    print('Estos son los países que generan ingresos de exportación en Synergy Logistics')
    print('Formato de lista: [pais, exportaciones, valor neto de exportaciones, porcentaje de exportación]')
    for porcentaje_exportacion in lista_exportaciones_ordenada:
      print(porcentaje_exportacion)
  elif opcion == '5':
    print('El total de ingresos por exportaciones por Synergy Logistics fue de', total_importaciones, 'unidades')
    print('Estos son los países que generan ingresos de importación en Synergy Logistics')
    print('Formato de lista: [pais, importaciones, valor neto de importaciones, porcentaje de importación]')
    for porcentaje_importacion in lista_importaciones_ordenada:
      print(porcentaje_importacion)

print('Gracias por visitar el portal de Synergy Logistics, esperamos verlo por aquí muy pronto.')
#para mostrar cada valor de exportaciones, importaciones, medios de transporte o ingresos, se establecieron iteraciones para acceder a los elementos de las listas de manera organizada. Por último, se muestra un mensaje de despedida para indicar el final de la ejecución del código.