# scriptparte1b.py
# utn - TUPAD - matematica1: trabajo practico intergrador2
# Bruno Pighin-  brunopighin@hotmail.com
# Aldo Manfredi - manfredialdo.1979@gmail.com

# condicion3: Si todos los conjuntos tienen al menos 5 elementos, entonces se
#   considera que hay una alta diversidad numérica.·
# condicion4: Si algún dígito aparece en todos los conjuntos, se marca como
#   dígito común.·
# condicion5: Si la intersección entre todos los conjuntos tiene exactamente un
#   elemento, se considera un dígito representativo del grupo.
def dni_a_conjunto():
    dni = input("Por favor, ingrese un DNI (8 dígitos numéricos): ")
    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("DNI inválido. Debe contener exactamente 8 dígitos numéricos.")
    return set(map(int, dni))

def condicion3(a, b):
    """"
    CONDICION3: hay una alta diversidad numérica?
    """
    if len(a)>=5 and len(b)>=5:
        return True

def condicion4(a,b):
    if len(a.intersection(b))>1:
        return True

def condicion5(a,b):
    if len(a.intersection(b))==1:
        return True

def inicio():
    dniA = dni_a_conjunto()
    dniB = dni_a_conjunto()
    if condicion3(dniA,dniB)==True:
        print("hay alta diversidad numerica")
    if condicion4(dniA,dniB)==True:
        print(f"los digitos comunes de ambos conjuntos son{dniA.intersection(dniB)}")
    if condicion5(dniA,dniB)==True:
        print(f"{dniA.intersection(dniB)} es el digito representativo compartidos por de ambos dnis")

inicio()
# TEST dni A = Bruno Pighin- DNI: 35940327; y dni Aldo Manfredi - DNI: 27028093;
