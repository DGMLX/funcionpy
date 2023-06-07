import funciones as fn

opcion = 0
while opcion != 4:
    print("1) Calcular IVA")
    print("2) Descuento")
    print("3) Calcular IMC")
    print("4) Salir")
    while True:
        try:
            opcion = int(input("Eliga una opcion: "))
            if opcion > 0 and opcion < 5:
                if opcion == 1:
                    fn.calcular_iva()
                    break
                elif opcion == 2:
                    fn.descuento()
                    break
                elif opcion == 3:
                    fn.calcular_imc()
                    break
                else:
                    print("Has salido del programa")
                    break
            else:
                print("Eliga una opcion válida.")
        except:
            print("Ingrese valor numerico")


