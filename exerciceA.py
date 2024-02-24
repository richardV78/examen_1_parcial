def main():
    # Crea una calculadora que pueda ralizar operaciones basicas como suma, resta, divicion y multiplicaion
    # perdmite que el usuario pueda elegir la opracon deseada mediante una sentencia de control 

    print("Hola, esta es tu calculadora")
    print("primer numero")
    num1 = int(input())
    operator = input("elige un operador matematico:  ")
    print("segundo numero")
    num2 = int(input())

    def suma(num1, num2): 
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2

    def multiplicacion(num1, num2):
        return num1 * num2

    def divicion(num1, num2):
        if num2 != 0:
            return num1 / num2 
        else:
            return "ERROR : divicion por cero"
            
    match operator:
        case "+": 
            print(f"la suma es igual a =  {suma(num1, num2)}") 
        
        case "-": 
            print(f"la resta es igual a =  {resta(num1, num2)}") 
        
        case "*": 
            print(f"la multiplicacion es igual a =  {multiplicacion(num1, num2)}") 

        case "/": 
            print(f"la divicion es igual a =  {divicion(num1, num2)}") 

if __name__ == "__main__":
    main()
