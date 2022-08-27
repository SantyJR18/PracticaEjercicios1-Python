""" Leer x cantidad de edades y mostrar el promedio de dichas edades. """

numerosEdad = int(input("Digite el numero de edades a evaluar para tomar el promedio: "))
x = 0
suma = 0
edad = 0
while x < numerosEdad:
    edad = int(input("Ingrese la edad: "))
    suma += edad
    x += 1 
print("la suma de las edades es: ", suma)

promedio = suma/numerosEdad
print("El promedio de las edades es de: ", promedio)