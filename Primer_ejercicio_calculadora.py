# Crea una calculadora que pueda ralizar operaciones basicas como suma, resta, divicion y multiplicaion
# perdmite que el usuario pueda elegir la opracon deseada mediante una sentencia de control 

print("Hola, esta es tu calculadora")
print("primer numero")
num1 = int(input())
operator = input("elige un operador matematico:  ")
print("segundo numero")
num2 = int(input())

def suma(a, b): 
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def divicion(a, b):
    if b != 0:
        return a / b 
    else:
        return "ERROR : divicion por cero"