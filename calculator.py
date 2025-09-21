
# Una función puede tomar parámetros como a y b
#este es el cambio hecho 
def add(a, b):
    # Suma los dos números recibidos como parámetros y devuelve el resultado
    return a + b

def subtract(a, b):
    # Resta el segundo número al primero y devuelve el resultado
    return a - b

def multiply(a, b):
    # Multiplica los dos números y devuelve el resultado
    return a * b

def divide(x, y):
    # Verifica que el divisor no sea cero antes de dividir
    if y == 0:
        # Si el divisor es cero, devuelve un mensaje de error
        return "Error! No puedes dividir por 0"
    # Si no, realiza la división y devuelve el resultado
    return x / y

def main():
    # Esta es la función principal que ejecuta la calculadora
    print("Selectiona una operacion") # Muestra el menú de opciones
    print("1. Add")      # Sumar
    print("2. Subtract") # Restar
    print("3. Multiply") # Multiplicar
    print("4. Divide")   # Dividir
    print("5. Exit")     # Salir

    while True:
        # Solicita al usuario que elija una opción
        choice = input("Entra tu seleccion: ")
        
        # Verifica si la opción es válida
        if choice in ['1', '2', '3', '4', '5']:
            try:
                # Pide los dos números al usuario
                num1 = int(input("Entra primer numero: "))
                num2 = int(input("Entra segundo numero: "))
            except ValueError:
                # Si el usuario no ingresa un número válido
                print("Por favor entra un numero bien mmg")
                continue
            # Ejecuta la operación seleccionada según la opción
            if choice == "1":
                # Suma
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                # Resta
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                # Multiplicación
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                # División
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == "5":
                # Salir del programa
                print("Adios!")
                break
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("Opcion invalida, por favor entra una opcion valida")

# Llama a la función principal para iniciar la calculadora
main()

#hoalalalka