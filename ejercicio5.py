""" Mostrar los numero pares comprendidos entre un valor inicial y un valor final de números
enteros. """

valorI= int(input("Digite un valor inicial: "))
valorF= int(input("Digite un valor final: "))

for i in range (valorI,valorF+1):
    if i%2==0:
        print(i)