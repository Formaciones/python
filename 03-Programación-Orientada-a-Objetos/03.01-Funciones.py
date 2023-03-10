#####################################################################
# Declaración de Funciones                                          #
#####################################################################
#                                                                   #
#   Sintaxis: def [nombre de la funcion](arg, args-1):              #
#                                                                   #
#   Ejemplos:                                                       #
#       def Saludar() -> None:                                      #
#       def Suma(a, b) -> int:                                      #
#                                                                   #
#####################################################################

from datetime import datetime

# Ejemplo de una función que no tiene parámetros(no recibe datos) y no retorna datos
def Func1():
    print("Hola a todos !!!")


# Ejemplo de una función que SI tiene parámetros(SI recibe datos) y no retorna datos
def Func2(nombre, numero):
    print(f"Me llamo {nombre} y mi número de la suerte es {numero}")


# Ejemplo de una función que SI tiene parámetros(SI recibe datos) y SI retorna datos
def Func3(frase):
    cant = 0
    cant = len(frase)
    return cant


# Ejemplo de una función que no tiene parámetros(no recibe datos) y SI retorna datos
def Func4():
    return datetime.now().date().strftime("%A")


Func1()

Func2("Borja", 20)

print(Func3("Hola a todos"))

dato = Func3("Hola a todos")
print(f"Dato: {dato}")

print(Func4())

dato2 = Func4()
print(f"Dato: {dato2}")


def Resta(a, b):
    return a - b

print(Resta(85, 10))
print(Resta(b=10, a=85))

def Resta1(a, b=10):
    return a - b

print(Resta1(85, 10))
print(Resta1(b=10, a=85))
print(Resta(85))
print(Resta(a=85))

def Resta2(a=25, b=10):
    return a - b

print(Resta2())
print(Resta2(85, 10))
print(Resta2(85))
print(Resta1(b=12))
