opcion = 01


print ("bienvenido")
print ("1.Binomio al cuadrado")
print ("2.cuadrado de una resta")
print ("3.Resultaddo de diferencia entre binomios")
print ("4.cubo de una suma ")
print ("5.cubo de una resta")
print ("6.Producto de dos binomios")
opcion =int(input("Seleccione la operacion a realizar --->"))

while True:
    if opcion == 1:
            va1 = (input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print (va1**2 ++ 2*va1*va2 ++ va2**2)
            break
    if opcion == 2:
            va1 = float(input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print (va1**2 -- 2*va1*va2 ++ va2**2)
            break
    if opcion == 3:
            va1 = float(input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print (va1**2 -- va2**2)
            break
    if opcion == 4:
            va1 = float(input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print (va1**3, 3*va1**2*va2,+ 3*va1*va2**2, va2**2)
            break
    if opcion == 5:
            va1 = float(input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print(va1**3,- 3*va1**2*va2,+ 3*va1*va2**2,- va2**2)
            break
    if opcion == 6:
            va1 = float(input("Escriba el factor 1 -->"))
            va2 = float(input("Escriba el factor 2 -->"))
            print (va1**2, 2*va1*va2, va2**2)
            break
  