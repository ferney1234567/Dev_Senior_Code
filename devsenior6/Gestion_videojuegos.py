
# PROYECTO FINAL - MoDULO 3: SISTEMA DE GESTIoN DE TIENDA DE VIDEOJUEGOS

# Docente: [Tu Nombre como Profesor]
# Fecha: [Fecha Actual]
# Nivel: Intermedio
# Tiempo Estimado: 2-3 horas



# 1. OBJETIVO GENERAL DEL PROYECTO

"""
Desarrollar un programa completo en Python que permita administrar el inventario
y las ventas de una tienda de videojuegos. Este proyecto integrador tiene como
meta aplicar de manera práctica todos los conceptos aprendidos en el modulo 3:

✓ Variables y tipos de datos
✓ Condicionales (if, elif, else)
✓ Ciclos (while, for)
✓ Funciones con parámetros y retorno
✓ Colecciones (diccionarios y listas)
✓ Validacion de datos
✓ Cálculos básicos

El resultado final será un sistema de consola completamente funcional que
demuestre el dominio de los fundamentos de Python.
"""


# 2. CONTEXTO Y ANÁLISIS DEL PROBLEMA

"""
CONTEXTO EMPRESARIAL:
Una tienda de videojuegos necesita un sistema informático para gestionar su
inventario y controlar las ventas diarias. Actualmente, toda la gestion se
realiza manualmente, lo que genera errores, pérdida de tiempo y dificultades
para obtener estadisticas de ventas.

PROBLEMA A RESOLVER:
- Controlar el inventario de videojuegos de manera automática
- Gestionar ventas con validaciones de stock
- Generar reportes y estadisticas de negocio
- Mantener la integridad de los datos

ESTRUCTURA DE DATOS PRINCIPAL:
Cada videojuego se representa como un diccionario anidado con la siguiente
informacion esencial para el negocio:
"""


# 3. ESPECIFICACIONES TÉCNICAS - ESTRUCTURA DE DATOS

# Modelo de datos para cada videojuego
# videojuego_modelo = {
#     "codigo": "VG001",           # Identificador único (string)
#     "nombre": "FIFA 26",         # Nombre del juego (string)
#     "plataforma": "PlayStation 5", # Plataforma (string)
#     "precio": 250000,            # Precio en pesos (int/float)
#     "cantidad": 10               # Unidades disponibles (int)
# }


# 4. ENUNCIADO DETALLADO DEL PROYECTO

"""
DESARROLLAR UN SISTEMA DE GESTIoN que permita a la tienda de videojuegos:

1. ADMINISTRAR INVENTARIO:
   - Agregar nuevos videojuegos al catálogo
   - Consultar el inventario completo
   - Buscar productos especificos
   - Actualizar precios
   - Eliminar productos obsoletos

2. GESTIONAR VENTAS:
   - Registrar ventas con validacion de stock
   - Generar facturas automáticas
   - Controlar inventario en tiempo real

3. OBTENER ESTADiSTICAS:
   - Reportes de inventario
   - Análisis de precios y stock
   - Métricas de negocio

El sistema debe funcionar a través de un menú interactivo que permita al
usuario navegar entre las diferentes opciones de manera intuitiva.
"""


# 5. INTERFAZ DE USUARIO - MENÚ PRINCIPAL

"""
El programa debe mostrar repetidamente el siguiente menú hasta que el usuario
elija salir:

===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por codigo
4. Actualizar precio
5. Registrar venta
6. Mostrar estadisticas
7. Eliminar videojuego
8. Salir

Seleccione una opcion (1-8): _
"""


# 6. REQUISITOS FUNCIONALES DETALLADOS

"""
Cada opcion del menú debe implementar las siguientes funcionalidades:
"""

# 6.1 AGREGAR VIDEOJUEGO
"""
Funcion: agregar_videojuego(videojuegos)
Descripcion: Solicita datos al usuario y agrega un nuevo videojuego al inventario

ENTRADAS (input del usuario):
- Codigo del videojuego
- Nombre del juego
- Plataforma
- Precio
- Cantidad inicial

VALIDACIONES REQUERIDAS:
✓ Codigo único (no debe existir en el diccionario)
✓ Precio > 0
✓ Cantidad >= 0
✓ Nombre y plataforma no vacios

SALIDA:
- Mensaje de confirmacion si se agrega correctamente
- Mensaje de error si hay validaciones fallidas
"""

# 6.2 MOSTRAR INVENTARIO
"""
Funcion: mostrar_inventario(videojuegos)
Descripcion: Muestra todos los videojuegos registrados en formato tabular

ENTRADAS:
- Diccionario de videojuegos

SALIDA:
- Lista formateada con todos los productos
- Mensaje especial si el inventario está vacio
"""

# 6.3 BUSCAR VIDEOJUEGO POR CoDIGO
"""
Funcion: buscar_videojuego(videojuegos)
Descripcion: Busca y muestra la informacion completa de un videojuego

ENTRADAS:
- Codigo del videojuego a buscar

SALIDA:
- Informacion completa del producto si existe
- Mensaje de "no encontrado" si no existe
"""

# 6.4 ACTUALIZAR PRECIO
"""
Funcion: actualizar_precio(videojuegos)
Descripcion: Permite modificar el precio de un videojuego existente

ENTRADAS:
- Codigo del videojuego
- Nuevo precio

VALIDACIONES:
✓ El videojuego debe existir
✓ Nuevo precio > 0

SALIDA:
- Confirmacion de actualizacion exitosa
"""

# 6.5 REGISTRAR VENTA
"""
Funcion: registrar_venta(videojuegos)
Descripcion: Procesa una venta y actualiza el inventario

ENTRADAS:
- Codigo del videojuego
- Cantidad a vender

VALIDACIONES:
✓ El videojuego debe existir
✓ Cantidad disponible >= cantidad solicitada
✓ Cantidad a vender > 0

ACCIONES:
- Restar cantidad del inventario
- Calcular total de la venta
- Mostrar factura detallada

SALIDA:
Factura con:
- Nombre del juego
- Precio unitario
- Cantidad vendida
- Total a pagar
"""

# 6.6 MOSTRAR ESTADiSTICAS
"""
Funcion: mostrar_estadisticas(videojuegos)
Descripcion: Genera reportes estadisticos del inventario

MÉTRICAS A CALCULAR:
✓ Total de videojuegos registrados
✓ Valor total del inventario (suma de precio * cantidad)
✓ Videojuego más costoso
✓ Videojuego con mayor cantidad disponible
✓ Promedio de precios de todos los juegos

SALIDA:
- Reporte formateado con todas las estadisticas
"""

# 6.7 ELIMINAR VIDEOJUEGO
"""
Funcion: eliminar_videojuego(videojuegos)
Descripcion: Remueve un videojuego del inventario

ENTRADAS:
- Codigo del videojuego a eliminar

VALIDACIONES:
✓ El videojuego debe existir

SALIDA:
- Confirmacion de eliminacion
- Mensaje de error si no existe
"""

# 6.8 SALIR
"""
Funcion: menu() debe terminar el programa
Descripcion: Finaliza la ejecucion del programa
"""


# 7. REQUISITOS TÉCNICOS OBLIGATORIOS

"""
FUNCIONES QUE DEBES IMPLEMENTAR (minimo obligatorio):

def agregar_videojuego(videojuegos: dict) -> None:
    pass

def mostrar_inventario(videojuegos: dict) -> None:
    pass

def buscar_videojuego(videojuegos: dict) -> None:
    pass

def actualizar_precio(videojuegos: dict) -> None:
    pass

def registrar_venta(videojuegos: dict) -> None:
    pass

def mostrar_estadisticas(videojuegos: dict) -> None:
    pass

def eliminar_videojuego(videojuegos: dict) -> None:
    pass

def menu() -> None:
    pass

RECOMENDACIONES DE IMPLEMENTACIoN:
- Usa funciones puras cuando sea posible
- Implementa validaciones robustas
- Maneja errores de manera elegante
- Usa nombres descriptivos para variables y funciones
- Comenta tu codigo adecuadamente
"""


# 8. DATOS DE PRUEBA INICIALES

"""
Para facilitar las pruebas, inicia tu programa con este diccionario:
"""
videojuegos_iniciales = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}


# 9. EJEMPLOS DE EJECUCIoN

"""
EJEMPLO 1: Agregar un videojuego
=====================================
Codigo: VG004
Nombre: God of War Ragnarök
Plataforma: PlayStation 5
Precio: 280000
Cantidad: 12

Resultado: "Videojuego agregado exitosamente"

EJEMPLO 2: Registrar una venta
=====================================
Codigo del videojuego: VG001
Cantidad a vender: 2

Resultado - Factura:
==================
Juego: FIFA 26
Precio unitario: $250,000
Cantidad: 2
Total: $500,000
==================
¡Venta registrada exitosamente!

EJEMPLO 3: Mostrar estadisticas
=====================================
Estadisticas del Inventario:
-----------------------------
Total de videojuegos: 3
Valor total del inventario: $6,950,000
Videojuego más costoso: FIFA 26 ($250,000)
Mayor cantidad disponible: FIFA 26 (10 unidades)
Promedio de precios: $230,000
"""


# 10. RETOS ADICIONALES (OPCIONALES - PARA NIVEL AVANZADO)

"""
Si completas el proyecto básico antes del tiempo estimado, implementa estas
funcionalidades adicionales:

🔹 BÚSQUEDA AVANZADA:
- Buscar videojuegos por plataforma
- Buscar videojuegos por rango de precios

🔹 ALERTAS DE INVENTARIO:
- Mostrar videojuegos con inventario bajo (cantidad < 3)
- Alertas automáticas al registrar ventas

🔹 DESCUENTOS INTELIGENTES:
- Aplicar 10% de descuento en ventas mayores a $500.000
- Descuentos por cantidad (3x2, etc.)

🔹 HISTORIAL DE VENTAS:
- Guardar todas las ventas en una lista de diccionarios
- Mostrar historial completo de ventas
- Calcular videojuego más vendido

🔹 EXPORTACIoN DE DATOS:
- Guardar inventario en archivo JSON
- Generar reportes en formato texto
"""


# 11. CONCEPTOS FUNDAMENTALES QUE PRACTICARÁS

"""
Este proyecto te permitirá demostrar dominio de:

📊 ESTRUCTURAS DE DATOS:
- Diccionarios anidados
- Listas para almacenamiento temporal
- Manipulacion de colecciones

🔧 FUNCIONES Y MODULARIDAD:
- Funciones con parámetros y retorno
- Separacion de responsabilidades
- Reutilizacion de codigo

⚡ CONTROL DE FLUJO:
- Condicionales (if/elif/else)
- Ciclos while para menús
- Ciclos for para iteracion

✅ VALIDACIoN Y MANEJO DE ERRORES:
- Validacion de entrada de usuario
- Manejo de casos edge
- Mensajes de error informativos

📈 LoGICA DE NEGOCIO:
- Cálculos matemáticos (totales, promedios)
- Logica condicional compleja
- Algoritmos de búsqueda y filtrado
"""


# 12. CRITERIOS DE EVALUACIoN

"""
El proyecto será evaluado según:

✅ FUNCIONALIDAD (60%):
- Todas las funciones implementadas correctamente
- Validaciones funcionando
- Menú operativo

✅ CoDIGO (25%):
- Legibilidad y organizacion
- Comentarios adecuados
- Nombres descriptivos
- Estructura modular

✅ VALIDACIONES (10%):
- Manejo correcto de errores
- Mensajes informativos
- Casos edge considerados

✅ CREATIVIDAD (5%):
- Funcionalidades adicionales implementadas
- Interfaz de usuario mejorada
"""


# 13. ENTREGA Y PRESENTACIoN

"""
INSTRUCCIONES DE ENTREGA:
1. El codigo debe estar bien comentado
2. Incluir datos de prueba iniciales
3. El programa debe ejecutarse sin errores
4. Demostrar todas las funcionalidades en funcionamiento

ARCHIVO A ENTREGAR:
- PROYECTOFINALmodulo3.py (codigo completo)
- Documentacion breve de las decisiones tomadas

TIEMPO DE PRESENTACIoN:
- 5 minutos explicando la logica implementada
- 5 minutos demostrando funcionalidades
- 5 minutos respondiendo preguntas del docente
"""


# 14. RECOMENDACIONES PARA EL DESARROLLO

"""
CONSEJOS PARA UN DESARROLLO EXITOSO:

1. PLANIFICACIoN:
   - Lee todo el enunciado antes de empezar
   - Diseña la estructura de funciones primero
   - Identifica las validaciones necesarias

2. DESARROLLO POR PARTES:
   - Implementa funcion por funcion
   - Prueba cada funcion individualmente
   - Integra gradualmente al menú principal

3. TESTING:
   - Prueba casos normales y casos edge
   - Verifica validaciones con datos inválidos
   - Confirma cálculos matemáticos

4. DEPURACIoN:
   - Usa print() temporales para debugging
   - Verifica tipos de datos
   - Revisa logica condicional

5. MEJORAS FINALES:
   - Limpia codigo no utilizado
   - Mejora mensajes al usuario
   - Agrega comentarios finales
"""


# ¡ÉXITO EN TU PROYECTO FINAL!

"""
Recuerda: este proyecto es tu oportunidad de demostrar todo lo aprendido.
Tomate tu tiempo, planifica bien, y disfruta el proceso de creacion.

Si tienes dudas durante el desarrollo, no dudes en consultar con tu docente.

¡Mucho éxito! 🚀
"""


# PROYECTO FINAL - MoDULO 3
# SISTEMA DE GESTIoN DE TIENDA DE VIDEOJUEGOS


# DICCIONARIO PRINCIPAL DEL INVENTARIO

videojuegos = {

    "videoJuego001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },

    "videoJuego002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },

    "videoJuego003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# LISTA PARA GUARDAR HISTORIAL DE VENTAS
historial_ventas = []



# FUNCIoN PARA VALIDAR NÚMEROS

def validar_numero(numero):
    if numero.replace(".", "", 1).isdigit():
        return True
    else:
        return False



# FUNCIoN: AGREGAR VIDEOJUEGO
def agregar_videojuego(videojuegos):

    print("\n-------- AGREGAR VIDEOJUEGO --------")
    codigo = input("Ingrese el codigo del videojuego: ").upper()
    if codigo == "":
        print("El codigo no puede estar vacio")
        return

    if codigo in videojuegos:
        print("El codigo ya existe")
        return

    nombre = input("Ingrese el nombre del videojuego: ")
    if nombre == "":
        print("El nombre no puede estar vacio")
        return

    plataforma = input("Ingrese la plataforma: ")
    if plataforma == "":
        print("La plataforma no puede estar vacia")
        return

    precio = input("Ingrese el precio: ")
    if validar_numero(precio) == False:
        print("El precio debe ser numérico")
        return

    precio = float(precio)

    if precio <= 0:
        print("El precio debe ser mayor a 0")
        return

    cantidad = input("Ingrese la cantidad disponible: ")

    if cantidad.isdigit() == False:
        print("La cantidad debe ser numérica")
        return

    cantidad = int(cantidad)

    if cantidad < 0:
        print("La cantidad no puede ser negativa")
        return

    # Agregar videojuego al diccionario
    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print("Videojuego agregado exitosamente")



# FUNCIoN: MOSTRAR INVENTARIO
def mostrar_inventario(videojuegos):
    print("\n--------- INVENTARIO DE VIDEOJUEGOS --------")

    if len(videojuegos) == 0:
        print("No hay videojuegos registrados")
        return

    print("-" * 95)
    print(f"{'CODIGO':<10} {'NOMBRE':<30} {'PLATAFORMA':<25} {'PRECIO':<12} {'STOCK':<10}")
    print("-" * 95)
    
    for codigo, datos in videojuegos.items():
        print(f"{codigo:<10} "
              f"{datos['nombre']:<30} "
              f"{datos['plataforma']:<25} "
              f"${datos['precio']:<10,.0f} "
              f"{datos['cantidad']:<10}")

    print("-" * 95)



# FUNCIoN: BUSCAR VIDEOJUEGO
def buscar_videojuego(videojuegos):

    print("\n----- BUSCAR VIDEOJUEGO -----")
    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo in videojuegos:
        juego = videojuegos[codigo]
        print("\n VIDEOJUEGO ENCONTRADO")
        print("-" * 40)
        print(f"Codigo: {codigo}")
        print(f"Nombre: {juego['nombre']}")
        print(f"Plataforma: {juego['plataforma']}")
        print(f"Precio: ${juego['precio']:,.0f}")
        print(f"Cantidad disponible: {juego['cantidad']}")
    else:
        print(" Videojuego no encontrado")



# FUNCIoN: ACTUALIZAR PRECIO
def actualizar_precio(videojuegos):

    print("\n-------- ACTUALIZAR PRECIO --------")
    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    nuevo_precio = input("Ingrese el nuevo precio: ")

    if validar_numero(nuevo_precio) == False:
        print("Debe ingresar un número válido")
        return

    nuevo_precio = float(nuevo_precio)

    if nuevo_precio <= 0:
        print("El precio debe ser mayor a 0")
        return

    videojuegos[codigo]["precio"] = nuevo_precio

    print(" Precio actualizado correctamente")


# FUNCIoN: REGISTRAR VENTA
def registrar_venta(videojuegos):

    print("\n------- REGISTRAR VENTA -------")

    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    juego = videojuegos[codigo]

    print(f"Stock disponible: {juego['cantidad']}")

    cantidad_vender = input("Ingrese cantidad a vender: ")

    if cantidad_vender.isdigit() == False:
        print("Debe ingresar números enteros")
        return

    cantidad_vender = int(cantidad_vender)

    if cantidad_vender <= 0:
        print("La cantidad debe ser mayor a 0")
        return

    if cantidad_vender > juego["cantidad"]:
        print("No hay suficiente stock")
        return

    subtotal = juego["precio"] * cantidad_vender

    descuento = 0

    if subtotal > 500000:

        descuento = subtotal * 0.10
        
    total = subtotal - descuento

    videojuegos[codigo]["cantidad"] -= cantidad_vender

    venta = {

        "codigo": codigo,
        "nombre": juego["nombre"],
        "cantidad": cantidad_vender,
        "total": total
    }

    historial_ventas.append(venta)

    print("\n------FACTURA DE VENTA------")
    print(f"Juego: {juego['nombre']}")
    print(f"Plataforma: {juego['plataforma']}")
    print(f"Precio unitario: ${juego['precio']:,.0f}")
    print(f"Cantidad vendida: {cantidad_vender}")
    print(f"Subtotal: ${subtotal:,.0f}")

    if descuento > 0:
        print(f"Descuento aplicado: ${descuento:,.0f}")

    print(f"TOTAL A PAGAR: ${total:,.0f}")

    print("=============================")

    print("Venta registrada exitosamente")

    if videojuegos[codigo]["cantidad"] < 3:
        print("⚠ ALERTA: Inventario bajo")



# FUNCIoN: MOSTRAR ESTADiSTICAS
def mostrar_estadisticas(videojuegos):

    print("\n------ ESTADiSTICAS DEL INVENTARIO ------")

    if len(videojuegos) == 0:
        print("No hay videojuegos registrados")
        return

    total_videojuegos = len(videojuegos)

    valor_total = 0
    suma_precios = 0

    juego_costoso = ""
    precio_mayor = 0

    juego_mayor_stock = ""
    mayor_stock = 0

    for codigo, datos in videojuegos.items():

        valor_total += datos["precio"] * datos["cantidad"]

        suma_precios += datos["precio"]

        if datos["precio"] > precio_mayor:

            precio_mayor = datos["precio"]
            juego_costoso = datos["nombre"]

        if datos["cantidad"] > mayor_stock:

            mayor_stock = datos["cantidad"]
            juego_mayor_stock = datos["nombre"]

    promedio_precios = suma_precios / total_videojuegos

    print("-" * 50)

    print(f"Total de videojuegos: {total_videojuegos}")

    print(f"Valor total del inventario: ${valor_total:,.0f}")

    print(f"Videojuego más costoso: {juego_costoso} (${precio_mayor:,.0f})")

    print(f"Mayor cantidad disponible: {juego_mayor_stock} ({mayor_stock} unidades)")

    print(f"Promedio de precios: ${promedio_precios:,.0f}")

    print("-" * 50)



# FUNCIoN: ELIMINAR VIDEOJUEGO
def eliminar_videojuego(videojuegos):

    print("\n----- ELIMINAR VIDEOJUEGO -----")

    codigo = input("Ingrese el codigo del videojuego: ").upper()

    if codigo not in videojuegos:
        print("El videojuego no existe")
        return

    print(f"Videojuego encontrado: {videojuegos[codigo]['nombre']}")

    confirmacion = input("¿Seguro que desea eliminarlo? (si/no): ").lower()

    if confirmacion == "si":

        del videojuegos[codigo]

        print("Videojuego eliminado correctamente")

    else:
        print("Eliminacion cancelada")


# FUNCIoN: MOSTRAR HISTORIAL DE VENTAS
def mostrar_historial_ventas():
    print("\n-------- HISTORIAL DE VENTAS --------")

    if len(historial_ventas) == 0:
        print("❌ No hay ventas registradas")
        return

    for venta in historial_ventas:
        print("-" * 40)
        print(f"Codigo: {venta['codigo']}")
        print(f"Juego: {venta['nombre']}")
        print(f"Cantidad vendida: {venta['cantidad']}")
        print(f"Total pagado: ${venta['total']:,.0f}")

    print("-" * 40)



# FUNCIoN PRINCIPAL: MENU
def menu():

    while True:
        print("\n")
        print("------ TIENDA DE VIDEOJUEGOS ------")
        print("1. Agregar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego")
        print("4. Actualizar precio")
        print("5. Registrar venta")
        print("6. Mostrar estadisticas")
        print("7. Eliminar videojuego")
        print("8. Mostrar historial de ventas")
        print("9. Salir")

        opcion = input("Seleccione una opcion (1-9): ")

        if opcion == "1":

            agregar_videojuego(videojuegos)

        elif opcion == "2":

            mostrar_inventario(videojuegos)

        elif opcion == "3":

            buscar_videojuego(videojuegos)

        elif opcion == "4":

            actualizar_precio(videojuegos)

        elif opcion == "5":

            registrar_venta(videojuegos)

        elif opcion == "6":

            mostrar_estadisticas(videojuegos)

        elif opcion == "7":

            eliminar_videojuego(videojuegos)

        elif opcion == "8":

            mostrar_historial_ventas()

        elif opcion == "9":
            print("Programa finalizado")
            break

        else:
            print("Opcion inválida")


menu()