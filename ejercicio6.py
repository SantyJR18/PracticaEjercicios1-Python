""" Leer dos números y decir cual es mayor y cual es menor. """

num1= int(input("Digite el valor del primer numero: "))
num2= int(input("Digite el valor del segundo numero: "))

if num1>num2:
    print("el numero mayor es:",num1)
    print("el numero menor es:",num2)
elif num1<num2:
    print("el numero mayor es:",num2)
    print("el numero menor es:",num1)