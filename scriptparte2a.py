
# scriptparte2a.py Operaciones con DNIs
# UTN TUPAD - matematica1: trabajo practico intergrador2
# Bruno Pighin-  brunopighin@hotmail.com
# Aldo Manfredi - manfredialdo.1979@gmail.com


# A. Operaciones con DNIs
# PERMITE
# · Ingreso de los DNIs (reales o ficticios).
# · Generación automática de los conjuntos de dígitos únicos.

#  CALCULO Y VISUALIZACION DE
# ·  unión, intersección, diferencias y diferencia simétrica.
# ·  suma total de los dígitos de cada DNI.
# ·  conteo de la frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.

#  CONDICIONES evaluacion y visualizacion de resultado de las condiciones
# · Si un dígito aparece en todos los conjuntos, mostrar "Dígito compartido".
# · Si algún conjunto tiene más de 6 elementos, mostrar "Diversidad numérica alta".

from random import randint

def dni_aleatorio():
    nrodni = randint(10000000, 65000000)
    return nrodni, set(map(int, str(nrodni)))

#CALCULOS
def calcular_union(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def calcular_interseccion(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def calcular_diferencia(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def calcular_diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1.symmetric_difference(conjunto2)

def sumar_digitos_dni(numero_dni):
    return sum(map(int, str(numero_dni)))

def contar_frecuencia_digitos(numero_dni):
    frecuencias = {}
    for digito_c in str(numero_dni):
        digito = int(digito_c)
        if digito in frecuencias:
            frecuencias[digito] += 1
        else:
            frecuencias[digito] = 1
    return frecuencias


# VISUALIZACION
def mostrar_resultados_conjuntos(conjunto_A_digitos, conjunto_B_digitos, original_dniA, original_dniB):
    print(f"Conjunto A (Dígitos DNI 1): {conjunto_A_digitos} \nConjunto B (Dígitos DNI 2): {conjunto_B_digitos}")

    union_result = calcular_union(conjunto_A_digitos, conjunto_B_digitos)
    print(f"Union (A U B): {union_result}")
    interseccion_result = calcular_interseccion(conjunto_A_digitos, conjunto_B_digitos)
    print(f"Interseccion (A ∩ B): {interseccion_result}")
    diferencia_ab_result = calcular_diferencia(conjunto_A_digitos, conjunto_B_digitos)
    print(f"Diferencia (A - B): {diferencia_ab_result}")
    diferencia_ba_result = calcular_diferencia(conjunto_B_digitos, conjunto_A_digitos)
    print(f"Diferencia (B - A): {diferencia_ba_result}")
    diferencia_simetrica_result = calcular_diferencia_simetrica(conjunto_A_digitos, conjunto_B_digitos)
    print(f"Diferencia Simétrica (A Δ B): {diferencia_simetrica_result}")
    print("-" * 30)

    # usamos 'original_dniA' y 'original_dniB' para las sumas
    print(f"Suma de dígitos del DNI 1 ({original_dniA}): {sumar_digitos_dni(original_dniA)}")
    print(f"Suma de dígitos del DNI 2 ({original_dniB}): {sumar_digitos_dni(original_dniB)}")
    print("-" * 30)

    # usamos 'original_dniA' y 'original_dniB' para las frecuencias
    print(f"Frecuencia de dígitos para DNI 1 ({original_dniA}):")
    frecuencias_dniA = contar_frecuencia_digitos(original_dniA)
    for digito, cuenta in sorted(frecuencias_dniA.items()):
        print(f"   Dígito {digito}: {cuenta} vez/veces")

    print(f"\nFrecuencia de dígitos para DNI 2 ({original_dniB}):")
    frecuencias_dniB = contar_frecuencia_digitos(original_dniB)
    for digito, cuenta in sorted(frecuencias_dniB.items()):
        print(f"   Dígito {digito}: {cuenta} vez/veces")
    print("-" * 30)

    # --- CONDICIONES ---
    print("\n--- Evaluación de Condiciones ---")
    # Condición1: Si un dígito aparece en todos los conjuntos
    if interseccion_result:
        print(f"Dígito(s) compartido(s): {interseccion_result}")
    else:
        print("No hay dígitos compartidos entre ambos DNIs.")

    # Condición2: Si algún conjunto tiene más de 6 elementos
    if len(conjunto_A_digitos) > 6 or len(conjunto_B_digitos) > 6:
        print("Diversidad numérica alta en al menos un DNI.")
    else:
        print("Ningún DNI tiene diversidad numérica alta (menos de 7 dígitos únicos).")
    print("-" * 30)


# la función 'inicio'
def inicio():
    print("0 - salir")
    print("1 - ingresar dos dni modo manual")
    print("2 - ingresar dos dni aleatorio")
    opcion = int(input("Elija opcion: "))

    dni_num1 = None # Inicializamos a None
    dni_num2 = None # Inicializamos a None
    conjunto_dni1 = None
    conjunto_dni2 = None

    if opcion == 1:
        str_dni1 = input("Ingrese DNI 1: ")
        str_dni2 = input("Ingrese DNI 2: ")
        dni_num1 = int(str_dni1) # Convertimos a int para las funciones de suma/frecuencia
        dni_num2 = int(str_dni2)
        conjunto_dni1 = set(map(int, str_dni1))
        conjunto_dni2 = set(map(int, str_dni2))
    elif opcion == 2:
        # dni_aleatorio devuelve (número, conjunto_de_dígitos)
        dni_num1, conjunto_dni1 = dni_aleatorio()
        dni_num2, conjunto_dni2 = dni_aleatorio()
        print(f"DNI 1 aleatorio generado: {dni_num1}")
        print(f"DNI 2 aleatorio generado: {dni_num2}")
    elif opcion == 0:
        return
    else:
        print("Opción no válida. Por favor, elija 1 o 2.")
        inicio()

    # Pasamos tanto los conjuntos de digitos unicos como los numeros de DNI originales
    if dni_num1 is not None and dni_num2 is not None:
        mostrar_resultados_conjuntos(conjunto_dni1, conjunto_dni2, dni_num1, dni_num2)

# TEST dni A = Bruno Pighin- DNI: 35940327; y dni Aldo Manfredi - DNI: 27028093;
inicio()
