""" Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni” """

nombre = input("Digite su primer nombre del estudiante: ")
nombre2 = input("Digite su segundo nombre: ")
apellido = input("Digite su primer apellido: ")
apellido2 = input("Digite su segundo apellido: ")
correo = "@est.uca.edu.ni"
print("Procesando información....")
print("Creando correo...")
print(nombre+"."+apellido+correo)