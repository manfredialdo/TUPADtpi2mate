#scriptparte2b.py operaciones con dos años de nacimiento
# UTN TUPAD - matematica1: trabajo practico intergrador2
# Aldo Manfredi - manfredialdo.1979@gmail.com
# Bruno Pighin-  brunopighin@hotmail.com

import datetime
def es_bisiesto(anio):
    return (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0)

def ingresar_anios_nacimiento():
    while True:
        anio1 = int(input("Ingrese año de nacimiento del integrante 1: "))
        anio2 = int(input("Ingrese año de nacimiento del integrante 2: "))
        return anio1, anio2

def verificar_bisiesto(anio1, anio2):
    if es_bisiesto(anio1) or es_bisiesto(anio2):
        print("\n---Tenemos un año especial, hay un bisiesto")

def calcular_producto_cartesiano(anios):
    anio_actual = datetime.datetime.now().year
    edades = [anio_actual - anio for anio in anios]

    print("\n--- Producto Cartesiano (Años x Edades) ---")
    for anio in anios:
        for edad in edades:
            print(f"({anio}, {edad})")

def verificar_grupo_z(anio1, anio2):
    if anio1 > 2000 and anio2 > 2000:
        print("\n---pertenece al Grupo Z")

def verificar_anios_iguales(anio1, anio2):
    if anio1 == anio2:
        print(f"\n---los dos nacieron mismo año... año: {anio1}")

def contar_anios_pares_impares(anio1, anio2):
    pares = 0
    impares = 0

    anios = [anio1, anio2]
    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"\n---Cantidad de años de nacimiento pares: {pares}")
    print(f"\n---Cantidad de años de nacimiento impares: {impares}")

def inicio():
    # 1. Ingreso de los años de nacimiento
    anio_integrante1, anio_integrante2 = ingresar_anios_nacimiento()
    anios_ingresados = [anio_integrante1, anio_integrante2]
    print(f"\nAños de nacimiento ingresados: {anio_integrante1}, {anio_integrante2}")
    verificar_bisiesto(anio_integrante1, anio_integrante2)
    calcular_producto_cartesiano(anios_ingresados)
    verificar_grupo_z(anio_integrante1, anio_integrante2)
    verificar_anios_iguales(anio_integrante1, anio_integrante2)
    contar_anios_pares_impares(anio_integrante1, anio_integrante2)

inicio()
# test:
# (2004, 2008) -> tres condiciones OK ... premio mayor
# (2004, 1999) -> bisiesto y par (2 condiciones)... premio consuelo
# (1823, 1999) -> ninguna condicion ... nada
