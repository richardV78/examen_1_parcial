def main():
    # 3er jercicio donde se pide calcular el 10 de descuento
    print("Hola, calculare tu descuento")

    print("Ingresa el total del precio de tus productos")
    print("Recibiras un 10 porciento de descuento si llevas mas de 500 cordobas")
    precio = int(input("dame la cantidad: "))

    def descuento(precio):
        if precio > 500:
            descuent = precio * 0.10
            descuent_final = precio - descuent
            print(f"tu descuento fue de  {descuent} y deberas pagar {descuent_final}")
        else:
            print("la cantidad no es suficiente para un descuento")


    print(descuento(precio)) 
    print("gracias")

if __name__ == "__main__":
    main()
