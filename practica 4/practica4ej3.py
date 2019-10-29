A = input("quiero calcular la base de un:")
if A == "Cuadrado":
     base = int(input("introduzca la base del cuadrado:"))
     altura = int(input("introduzca la altura del cuadrado:"))
     Area = (base*altura)
     print ("el area del cuadrado es", Area,)
elif A == "triangulo":
     base = int(input("introduzca la base del triangulo:"))
     altura = int(input("introduzca la altura del triangulo:"))
     Area = (base*altura)/2
     print ("el area del triangulo es", Area,)
else:
    print ("error")
    
