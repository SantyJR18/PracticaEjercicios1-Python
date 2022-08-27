def menuProgram():
  opc = True
  
  while opc == True:
    print("Santy EXEC\n")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))

    beca = False

    if(carrera.lower() == "ingenieria en sistemas"):
      if(promedio > 95):
        beca = True
      else:
        beca = False
    else:
      if(promedio > 85):
        beca = True
      else:
        beca = False

    print("\nNombre: ", nombre)
    print("Apellido: ", apellido)
    print("Carrera: ", carrera)
    print("Promedio: ", promedio)
    if(beca == True):
      message = "El estudiante podrá a obtar a una beca."
    else:
      message = "El estudiante no podrá obtar a una beca."
    print("Beca: ", message)

    sett = input("\n\n¿Desea agregar otro registro? (Y = Si / N = No): ")

    if(sett.lower() == "y"):
      print("\n")
      opc = True
    elif(sett.lower() == "n"):
      opc = False
      break
    else:
      opc = False
      break

    
menuProgram()