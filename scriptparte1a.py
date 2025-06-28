# scriptparte1a.py  - caso practico Expresiones lógicas en lenguaje natural:
# utn - TUPAD - matematica1: trabajo practico intergrador2
# Bruno Pighin-  brunopighin@hotmail.com
# Aldo Manfredi - manfredialdo.1979@gmail.com

def dni_a_conjunto():
    # solocita un dni y devuelve conjunto
    dni = input("Por favor, ingrese un DNI (8 dígitos numéricos): ")
    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("DNI inválido. Debe contener exactamente 8 dígitos numéricos.")
    return set(map(int, dni))

def condicion1(a,b):
    """
    CONDICION1: una función que a partir de dos conjuntos nos devuelva True si la
    suma de los elementos de la diferencia de A - B es impar
    """
    if sum(a.difference(b)) % 2!=0:
        return True

def condicion2(a, b):
    """"
    CONDICION2: una función que a partir de dos conjuntos nos devuelva True si
    la intersección entre A y B tiene al menos 5 elementos
    """
    if len(a.intersection(b))>=5:
        return True

def inicio():
    # pedir dos dnis
    dniA = dni_a_conjunto()
    dniB = dni_a_conjunto()
    # las condiciones de nuestro caso practico
    if condicion1(dniA, dniB) == True and condicion2(dniA, dniB)==True:
        return "a estudiar"
    else:
        return "ver pelis"
# TEST dni A = Bruno Pighin- DNI: 35940327; y dni Aldo Manfredi - DNI: 27028093;
inicio()


