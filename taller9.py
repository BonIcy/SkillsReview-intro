""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

nombre = str(imput("Coloca tu nombre"))
apellidos = str(imput("Coloca tus apellidos"))
edad = str(imput("¿Cual es tu edad(Pon solo el numero)?"))
telefono = str(input("Pon tu número de telefono celular o fijo"))
añoDeIngreso = str(input("Escribe el año en que ingresaste a la empresa"))

print("Tu nombre completo es=" nombre + apellidos, "\n Tu año de ingreso fue en el año" + añoDeIngreso)
