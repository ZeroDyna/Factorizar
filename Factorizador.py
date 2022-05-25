opcion = 0


while True:

    print ("bienvenido")
    print ("1.Binomio al cuadrado")
    print ("2.cuadrado de una resta")
    print ("3.Resultaddo de diferencia entre binomios")
    print ("4.cubo de una suma ")
    print ("5.cubo de una resta")
    print ("6.Producto de dos binomios")
    print ("7.Finalizar el programa")
    opcion =int(input("Seleccione la operacion a realizar --->"))

    while True:
        if opcion == 1:
             va1 = input("Escriba el factor 1 -->")
             va2 = float(input("Escriba el factor 2 -->"))
             print (va1, chr(94), 2 ,chr(43), 2*va2,chr(40), va1,chr(41),chr(43),  va2**2 )
             break
             
        elif opcion == 2:
              va1 = input("Escriba el factor 1 -->")
              va2 = float(input("Escriba el factor 2 -->"))
              print (va1, chr(94), 2 ,chr(45), 2*va2,chr(40), va1,chr(41),chr(43),  va2**2 )
              break
        elif opcion == 3:
                va1 = input("Escriba el factor 1 -->")
                va2 = input("Escriba el factor 2 -->")
                print (va1, chr(94), 2 ,chr(45) , va2, chr(94), 2)
                break
        elif opcion == 4:
                va1 = input("Escriba el factor 1 -->")
                va2 = input("Escriba el factor 2 -->")
                print (va1,chr(94),3,chr(43), 3, chr(40), va1, chr(41) ,chr(94), 2, chr(40), va2,chr(41), chr(43), 3, chr(40), va1, chr(41),  chr(40), va2,chr(41),chr(94), 2, chr(43), va2 ,chr(94),2)
                break
        elif opcion == 5:
                va1 = float(input("Escriba el factor 1 -->"))
                va2 = float(input("Escriba el factor 2 -->"))
                print(va1,chr(94),3,chr(45), 3, chr(40), va1, chr(41) ,chr(94), 2, chr(40), va2,chr(41), chr(43), 3, chr(40), va1, chr(41),  chr(40), va2,chr(41),chr(94), 2, chr(45), va2 ,chr(94),2)
                break
        elif opcion == 6:
                va1 = input("Escriba el factor 1, 3 -->")
                va2 = input("Escriba el factor 2 -->")
                va4 = input("Escriba el factor 4 -->")
                print (va1,chr(94),2, chr(43),chr(40), va1,chr(41),chr(40), va2,chr(43), va1 ,chr(41),chr(43),chr(40), va2,chr(41),chr(40), va4,chr(41))
                break
        else:
            print ("gracias, hasta pronto")
            break