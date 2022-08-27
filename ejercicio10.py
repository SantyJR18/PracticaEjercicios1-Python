'''
Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda después del retiro.
'''

import uuid

cuentasBancarias = [];
count12 = 0

def crearCuenta():
  sett = True
  while sett == True:
    print("\nAñadir una Cuenta...")
    nombres = input("\n\nIngrese su nombre: ")
    apellidos = input("Ingrese su apellido: ")
    numCuenta = str(uuid.uuid4())
    saldo = 0
    print("\n\nNombre Completo: ", nombres + " " + apellidos)
    print("Numero de Cuenta: ", numCuenta)
    print("Saldo: ", saldo)

    cuentBancaria = {
      "nombreCompleto": nombres + " " + apellidos,
      "numCuenta": numCuenta,
      "saldo": saldo
    }

    cuentasBancarias[len(cuentasBancarias):] = [cuentBancaria]

    letter = input("\n¿Desea añadir otra cuenta? (Y = Si / N = No): ")

    if(letter.lower() == "y"):
      print("\n\n")
      sett = True;
    else:
      print("\n\n")
      sett = False;

def encontrado(numCuenta):
  found = False

  for cnta in cuentasBancarias: 
    if(cnta['numCuenta'] == numCuenta):
      found = True
      break
    else:
      found = False

  return found

def cuentaBanc(numCuenta):
  for cnta in cuentasBancarias:
    if(cnta['numCuenta'] == numCuenta):
      cuenta1 = cnta
      break

  return cuenta1

def showCuenta():
  print("\n\nVer Cuenta...")
  numC = input("\nIngrese el numero de cuenta: ")
  found = encontrado(numC)
  if(found == True):
    cuenta = cuentaBanc(numC)
    print("\n\nNombre Completo: ", cuenta["nombreCompleto"])
    print("Numero de Cuenta: ", cuenta["numCuenta"])
    print("Saldo: ", cuenta["saldo"])
    print("\n\n")
  else:
    print("\n\nNo existe ninguna cuenta con ese número...\n\n")

def añadirSaldo():
  print("\n\nAñadir Saldo...")
  numC = input("\nIngrese el numero de cuenta: ")
  found = encontrado(numC)
  if(found == True):
    newSaldo = int(input("\nIngrese el nuevo saldo a ingresar: "))
    for cuenta in cuentasBancarias:
      if(cuenta['numCuenta'] == numC):
        cuenta['saldo'] = newSaldo
        break
    print("\n\nSaldo agregado correctamente...\n\n")
  else:
    print("\n\nNo existe ninguna cuenta con ese número...\n\n")


def retirarSaldo():
  print("\n\nRetirar Saldo...")
  numC = input("\nIngrese el numero de cuenta: ")
  found = encontrado(numC)
  if(found == True):
    retiroSaldo = int(input("\nIngrese el saldo a retirar: "))
    for cuenta in cuentasBancarias:
      if(cuenta['numCuenta'] == numC):
        if(cuenta['saldo'] < retiroSaldo):
          print("\n\nNo se puede retirar esa cantidad ya que no posee saldo suficiente para esa transacción\n\n")
        else:
          cuenta['saldo'] -= retiroSaldo
          print("\n\nSaldo retirado Satisfactoriamente...\n\n")
        break
  else:
    print("\n\nNo existe ninguna cuenta con ese número...\n\n")

def menuCuenta():
  while True:
    print("--------------------------------------------------------")
    print("\nSanty EXEC\n")
    print("--------------------------------------------------------")
    print("\n1) Crear una cuenta bancaria.")
    print("2) Ver saldo de cuenta bancaria.")
    print("3) Añadir saldo a cuenta bancaria.")
    print("4) Realizar retiro en una cuenta bancaria.")
    print("5) Salir del Programa.\n")
    print("--------------------------------------------------------")
    opc = int(input("\nIngrese la opción deseada: "))
    print("\n--------------------------------------------------------")
    
    if(opc == 1):
      crearCuenta()
    elif(opc == 2):
      showCuenta()
    elif(opc == 3):
      añadirSaldo()
    elif (opc == 4):
      retirarSaldo()
    else:
      break

menuCuenta()