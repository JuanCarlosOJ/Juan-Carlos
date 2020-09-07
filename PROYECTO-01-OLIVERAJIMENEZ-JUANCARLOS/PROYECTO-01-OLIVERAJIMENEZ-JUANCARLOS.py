from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

                                 #Código para análisis de ventas
counter = 0
total_de_ventas = []
for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      counter +=1
  
  plantilla = [producto[1], counter]
  total_de_ventas.append(plantilla)
  counter = 0
  total_de_mas_ventas = total_de_ventas.copy()

                                  #Los productos más vendidos
total_de_ventas_más = []
while total_de_mas_ventas:
  máximo = total_de_mas_ventas [0][1]
  lista_más_vendidas = total_de_mas_ventas [0]
  for Venta_mas in total_de_mas_ventas:
    if Venta_mas[1] > máximo:
      máximo = Venta_mas[1]
      lista_más_vendidas = Venta_mas
  total_de_ventas_más.append(lista_más_vendidas)
  total_de_mas_ventas.remove(lista_más_vendidas)

                                  #Los productos menos vendidos
total_de_ventas_menos = []
while total_de_ventas:
  mínimo = total_de_ventas [0][1]
  lista_menos_vendidas = total_de_ventas[0]
  for Venta_menos in total_de_ventas:
    if Venta_menos[1] < mínimo:
      mínimo = Venta_menos[1]
      lista_menos_vendidas = Venta_menos
  total_de_ventas_menos.append(lista_menos_vendidas)
  total_de_ventas.remove(lista_menos_vendidas)

                                  #Código para análisis de búsquedas
counter_b = 0
total_de_búsquedas = []

for producto in lifestore_products:
  for búsqueda in lifestore_searches:
    if producto[0] == búsqueda[1]:
      counter_b += 1
  
  plantilla_búsquedas = [producto[1], counter_b]
  total_de_búsquedas.append(plantilla_búsquedas)
  counter_b = 0
  total_de_busquedas_menos = total_de_búsquedas.copy()

                                    #Los productos más buscados
Los_mas_buscados = []
while total_de_búsquedas:
  maximo = total_de_búsquedas [0][1]
  lista_mas_buscadas = total_de_búsquedas [0]
  for Busqueda_mas in total_de_búsquedas:
    if Busqueda_mas[1] > maximo:
      maximo = Busqueda_mas[1]
      lista_mas_buscadas = Busqueda_mas
  Los_mas_buscados.append(lista_mas_buscadas)
  total_de_búsquedas.remove(lista_mas_buscadas)

                                  #Los productos menos buscados
Los_menos_buscados = []
while total_de_busquedas_menos:
  minimo = total_de_busquedas_menos [0][1]
  lista_menos_buscadas = total_de_busquedas_menos [0]
  for Busqueda_menos in total_de_busquedas_menos:
    if Busqueda_menos[1] < minimo:
     minimo = Busqueda_menos[1]
     lista_menos_buscadas = Busqueda_menos
  Los_menos_buscados.append(lista_menos_buscadas)
  total_de_busquedas_menos.remove(lista_menos_buscadas)

                                #Código para análisis de reseñas
contador_puntos = 0
sumador_puntos = 0
puntaje_final = []

for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      contador_puntos += 1
      sumador_puntos += venta[2]
  promedio_puntos = float(sumador_puntos/contador_puntos)
  lista_puntos = [producto[1], promedio_puntos]
  puntaje_final.append(lista_puntos)
  copia_puntaje_final = puntaje_final.copy()

                              #Los productos con las mejores reseñas
total_reseñas = []
while puntaje_final:
  máximo = puntaje_final [0][1]
  mejores_reseñas_list = puntaje_final [0]
  for Reseña_mayor in puntaje_final:
    if Reseña_mayor[1] > máximo:
      máximo = Reseña_mayor[1]
      mejores_reseñas_list = Reseña_mayor
  total_reseñas.append(mejores_reseñas_list)
  puntaje_final.remove(mejores_reseñas_list)

                              #Los productos con las peores reseñas
total_reseñas_peores = []
while copia_puntaje_final:
  mínimo = copia_puntaje_final [0][1]
  peores_reseñas_list = copia_puntaje_final [0]
  for Reseña_peor in copia_puntaje_final:
    if Reseña_peor[1] < mínimo:
      mínimo = Reseña_peor[1]
      peores_reseñas_list = Reseña_peor
  total_reseñas_peores.append(peores_reseñas_list)
  copia_puntaje_final.remove(peores_reseñas_list)

                            #Código para estadísticas de ingresos
counter = 0
total_de_ventas = []

for producto in lifestore_products:
  for venta in lifestore_sales:
    if producto[0] == venta[1]:
      counter +=1
  plantilla = [producto[0], counter]
  total_de_ventas.append(plantilla)
  counter = 0
  total_de_mas_ventas = total_de_ventas.copy()

cuenta_total = 0

for venta in total_de_ventas:
  for producto in lifestore_products:
    if venta[0] == producto[0]:
      producto_de_ventas = int(venta[1]*producto[2])
      cuenta_total += producto_de_ventas

                                  # Ingresos por años
                                      #2020
contador_productos_vendidos = 0
ganancias_2020 = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][6:10]) == 2020:
      contador_productos_vendidos += 1
  venta_por_producto_año = int(contador_productos_vendidos*producto[2])
  ganancias_2020 += venta_por_producto_año
  contador_productos_vendidos = 0
                                      #2019
contador_productos_vendidos = 0
ganancias_2019 = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][6:10]) == 2019:
      contador_productos_vendidos += 1
  venta_por_producto_año = int(contador_productos_vendidos*producto[2])
  ganancias_2019 += venta_por_producto_año
  contador_productos_vendidos = 0

                                      #2002
contador_productos_vendidos = 0
ganancias_2002 = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][6:10]) == 2002:
      contador_productos_vendidos += 1
  venta_por_producto_año = int(contador_productos_vendidos*producto[2])
  ganancias_2002 += venta_por_producto_año
  contador_productos_vendidos = 0

                                  #Ingresos enero
contador_productos_vendidos = 0
ganancias_enero = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 1:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_enero += venta_por_producto_mes
  contador_productos_vendidos = 0

                                 #Ingresos febrero
contador_productos_vendidos = 0
ganancias_febrero = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 2:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_febrero += venta_por_producto_mes
  contador_productos_vendidos = 0

                                  #Ingresos marzo
contador_productos_vendidos = 0
ganancias_marzo = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 3:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_marzo += venta_por_producto_mes
  contador_productos_vendidos = 0

                                   #Ingresos abril
contador_productos_vendidos = 0
ganancias_abril = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 4:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_abril += venta_por_producto_mes
  contador_productos_vendidos = 0

                                    #Ingresos mayo
contador_productos_vendidos = 0
ganancias_mayo = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 5:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_mayo += venta_por_producto_mes
  contador_productos_vendidos = 0

                                    #Ingresos junio
contador_productos_vendidos = 0
ganancias_junio = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 6:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_junio += venta_por_producto_mes
  contador_productos_vendidos = 0

                                    #Ingresos julio
contador_productos_vendidos = 0
ganancias_julio = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 7:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_julio += venta_por_producto_mes
  contador_productos_vendidos = 0

                                  #Ingresos agosto
contador_productos_vendidos = 0
ganancias_agosto = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 8:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_agosto += venta_por_producto_mes
  contador_productos_vendidos = 0

                               #Ingresos septiembre
contador_productos_vendidos = 0
ganancias_septiembre = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 9:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_septiembre += venta_por_producto_mes
  contador_productos_vendidos = 0

                                #Ingresos octubre
contador_productos_vendidos = 0
ganancias_octubre = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 10:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_octubre += venta_por_producto_mes
  contador_productos_vendidos = 0

                                #Ingresos noviembre
contador_productos_vendidos = 0
ganancias_noviembre = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 11:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_noviembre += venta_por_producto_mes
  contador_productos_vendidos = 0

                                #Ingresos diciembre
contador_productos_vendidos = 0
ganancias_diciembre = 0


for producto in lifestore_products:
  for fecha in lifestore_sales:
    if producto[0] == fecha[1] and int(fecha[3][3:5]) == 12:
      contador_productos_vendidos += 1
  venta_por_producto_mes = int(contador_productos_vendidos*producto[2])
  ganancias_diciembre += venta_por_producto_mes
  contador_productos_vendidos = 0

                                #Ventas por cada mes
       #Obtenidos a partir de un análisis previo con el código para estadísticas de ingresos
Ingresos_por_cada_mes = [['Enero', 120237], ['Febrero', 110139], ['Marzo', 164729], ['Abril', 193295], ['Mayo', 96394], ['Junio', 36949], ['Julio', 26949], ['Agosto', 3077], ['Septiembre', 4199], ['Octubre', 0], ['Noviembre', 4209], ['Diciembre', 0]]

Ingresos_ordenados = []
while Ingresos_por_cada_mes:
  máximo = Ingresos_por_cada_mes[0][1]
  lista_orden_mes = Ingresos_por_cada_mes[0]
  for mes in Ingresos_por_cada_mes:
    if mes [1] > máximo:
      máximo = mes [1]
      lista_orden_mes = mes
  Ingresos_ordenados.append(lista_orden_mes)
  Ingresos_por_cada_mes.remove(lista_orden_mes)

#Mensaje de bienvenida e inicio de sesión
Mensaje_de_bienvenida = 'Bienvenido, por favor registrese o inicie sesión para ingresar'
print (Mensaje_de_bienvenida)


#Registro e Inicio de sesión
es_admin = 0
Pregunta_de_Usuario = input('¿Usted cuenta con una cuenta de usuario? (S/N) ')

if Pregunta_de_Usuario == 'S':
  print ('Escriba su usuario aquí')

  Usuario = 'Juan Carlos OJ'
  Contraseña = 'Olivera123'
  usuario = input('Ingrese su nombre de usuario: ')
  contraseña = input('Ingrese una contraseña: ')
  
  if Usuario == usuario and Contraseña == contraseña:
	  es_admin = 1
	  
  intentos = 0
  while Usuario != usuario and Contraseña != contraseña and intentos <= 3:
    print('Usuario y/o contraseña incorrectos, por favor intente otra vez')
    usuario = input('Ingrese su nombre de usuario: ')
    contraseña = input('Ingrese su contraseña: ')
    intentos += 1
  if intentos <= 3:
	  es_admin = 1
	  print('Bienvenido '+ usuario)
  if intentos > 3:
    print('Demasiados intentos, por favor intente más tarde o registre un nuevo usuario y contraseña')
  breakpoint

if Pregunta_de_Usuario == 'N':
  es_admin = 1
  print('Por favor, introduzca un nombre de usuario y contraseña')
  usuario = input('Escriba su nombre de usuario: ')
  contraseña = input('Escriba una contraseña: ')
  print('Bienvenido '+ usuario)
  

  #Menú de opciones
Opción = 0
while Opción != "8" and es_admin == 1:
  Pregunta_a_usuario = '\n Por favor seleccione una opción. \n 1. Ver el top 50 de los productos más vendidos. \n 2. Ver el top 50 de los productos más buscados. \n 3. Ver el top 50 de los productos con menos ventas. \n 4. Ver el top 50 de los productos menos buscados. \n 5. Ver la lista de los 20 productos con las mejores reseñas. \n 6. Ver la lista de los 20 productos con las peores reseñas. \n 7. Ver un análisis de los ingresos en general y un análisis de los ingresos mensuales comenzando por el mes con mayores ingresos.\n 8. Salir\n'
  print(Pregunta_a_usuario)
  Opción = input('Opción: ')
  if Opción == '1':
    print('\n Aquí los 50 productos más vendidos')
    for venta_mas in total_de_ventas_más[0:50]:
      print('\n', venta_mas)
  if Opción == '2':
    print('\n Aquí los 50 productos más buscados')
    for mas_buscado in Los_mas_buscados[0:50]:
      print('\n', mas_buscado)
  if Opción == '3':
    print('\n Aquí los 50 productos menos vendidos')
    for venta_menos in total_de_ventas_menos[0:50]:
      print('\n', venta_menos)
  if Opción == '4':
    print('\n Aquí los 50 productos menos buscados')
    for menos_buscado in Los_menos_buscados[0:50]:
      print('\n', menos_buscado)
  if Opción == '5':
    print('\n Aquí los 20 productos con las mejores reseñas')
    for mejor_reseña in total_reseñas[0:20]:
      print('\n', mejor_reseña)
  if Opción == '6':
    print('\n Aquí los 20 productos con las peores reseñas')
    for peor_reseña in total_reseñas_peores[0:20]:
      print('\n', peor_reseña)
  if Opción == '7':
    print('\n Aquí las estadísticas de ingresos')
    print('\n El total de ingresos es ', cuenta_total, 'unidades')
    print('\n El total de ingresos en 2020 fue de ', ganancias_2020, 'unidades')
    print('\n El total de ingresos en 2019 fue de ', ganancias_2019, 'unidades')
    print('\n El total de ingresos en 2002 fue de ', ganancias_2002, 'unidades')
    for ingreso_mes in Ingresos_ordenados:
      print('\n', ingreso_mes)

print('¡Gracias por visitarnos! Esperamos verlo por aquí muy pronto.')
