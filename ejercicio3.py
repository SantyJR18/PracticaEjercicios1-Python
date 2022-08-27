""" Aplicar el IVA al precio de un producto. """

precio = int(input("Digite el precio del producto: C$"))
total=(0.15*precio)+precio
print("El total del producto con IVA es de: C$",total)