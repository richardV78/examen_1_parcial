def main():
    #calcular si la nota del estudiante es o no apta para un beca
    print("Hola capital humano")
    nota_alumno = int(input("Dame tu promedio academico "))

    def beca(nota_alumno):
        if nota_alumno >= 95:
            print("FELICIDADES APLICAS PARA UNA BECA UNIVERSITARIA!!!")
        else:
            print("LO SENTIMOS TU PROMEDIO NO ES SUFICIENTE PARA UNA BECA")

    def noticia():
        print(beca(nota_alumno))
    noticia()

if __name__ == "__main__":
    main()
