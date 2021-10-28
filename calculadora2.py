print("***********")
print("Calculadora")
print("***********\n")

print("Menu de Opciones\n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División Entera")
print("6. Exponente")
print("7. Modulo o Resto")

num = int(input("\nPor favor seleccione la opcion deseada: "))

if num ==1:
          print ("\nElegiste Suma")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num += int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la suma es: ", num)

elif num ==2:
          print ("\nElegiste Resta")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num -= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la Resta es: ", num)

elif num ==3:
          print ("\nElegiste Multiplicacion")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num *= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la Multiplicación es: ", num)

elif num ==4:
          print ("\nElegiste División")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num /= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la División es: ", num)

elif num ==5:
          print ("\nElegiste División Entera")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num //= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la División Entera es: ", num)

elif num ==6:
          print ("\nElegiste Exponente")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num **= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado de la Exponente es: ", num)

elif num ==7:
          print ("\nElegiste Modulo")
          num = int(input("\nPor favor ingrese el primer numero: "))
          num %= int(input("\nPor favor ingrese el segundo numero: "))
          print ("\nEl resultado del Modulo es: ", num)

else:
    print("Usted introdujo una opcion erronea")

















