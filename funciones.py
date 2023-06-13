
def calcular_iva():
    while True:
        try:
            precioProducto = int(input("Ingrese precio del producto "))
            if precioProducto < 0:
                print("Ingrese precio valido")
            else:
                print(f"El iva del producto es : {precioProducto*0.19}")
            break
        except:
            print("Ingrese valo numerico")


def descuento():
    while True:
        try:
            precioProducto = int(input("Ingrese precio del producto "))
            descuento = int(input("Ingrese descuento en % "))
            if precioProducto < 0:
                print("Ingrese precio valido")
            else:
                print(f"El precio del producto queda en : {precioProducto - (precioProducto*(descuento/100))}")
            break
        except:
            print("Ingrese valo numerico")

def calcular_imc():
    while True:
        try:
            peso = int(input("Ingrese su peso en KG "))
            altura = float(input("Ingrese su altura en metros "))
            if peso < 0 or altura < 0 :
                print("Ingrese precio valido")
            else:
                print(f"Su imc es de : {peso/(altura*altura)}")
                calcularEstado(peso/(altura*altura))
            break
        except:
            print("Ingrese valo numerico")


def calcularEstado(imc):
    if imc < 18.5:
        print("BAJO PESO")
    elif imc >= 18.5 and imc <= 24.9:
        print("PESO ADECUADO")
    elif imc >= 25 and imc <= 29.9:
        print("SOBREPESO")
    elif imc >= 30 and imc <= 34.9:
        print("OBESIDAD GRADO 1")
    elif imc >= 35 and imc <= 39.9:
        print("OBESIDAD GRADO 2")
    elif imc <= 40:
        print("OBESIDAD GRADO 3")
