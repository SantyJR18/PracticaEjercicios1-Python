"""Mostrar el total a pagar por la compra de n cantidad de productos a un precio
desconocido."""

numero = int(input("Ingrese la cantidad de producto que desea: "));

acc = 0

for count in range(numero):
  print("\n")
  print("Cliente: ", (count + 1))
  print("\n")
  producto = input("Ingrese el nombre del producto: ")
  precio = int(input("Ingrese el precio del producto: "))
  acc += precio  

print("\n")
print("El precio total de los productos a pagar es de: ", acc)