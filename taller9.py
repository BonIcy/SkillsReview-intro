""" " 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes: 
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

nombre = input("Coloca tu nombre:")
apellidos =input("Coloca tus apellidos: ")
edad = input("¿Cual es tu edad(Pon solo el numero)?: ")
telefono = input("Pon tu número de telefono celular o fijo: " )
añoDeIngreso = input("Escribe el año en que ingresaste a la empresa: ")

print("Tu nombre completo es :", nombre,  apellidos, "y tu año de ingreso fue en el año", añoDeIngreso)