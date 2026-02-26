# 1. Sumar n números
def sumar_numeros():
    n = int(input("¿Cuántos números deseas sumar? "))
    suma = 0
    for i in range(n):
        num = float(input(f"Ingrese número {i+1}: "))
        suma += num
    print("La suma total es:", suma)


# 2. Invertir un número
def invertir_numero():
    numero = input("Ingrese un número: ")
    invertido = numero[::-1]
    print("Número invertido:", invertido)


# 3. Información personal
def informacion_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    profesion = input("Ingrese su profesión: ")
    
    print(f"Hola {nombre}, tienes {edad} años y trabajas como {profesion}. ¡Mucho éxito!")


# 4. Obtener valores únicos
def valores_unicos():
    cantidad = int(input("¿Cuántos números ingresará? "))
    numeros = []
    
    for i in range(cantidad):
        num = input(f"Ingrese número {i+1}: ")
        numeros.append(num)
    
    unicos = list(set(numeros))
    print("Valores únicos:", unicos)


# Menú
def main():
    while True:
        print("\n1. Sumar números")
        print("2. Invertir número")
        print("3. Información usuario")
        print("4. Valores únicos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sumar_numeros()
        elif opcion == "2":
            invertir_numero()
        elif opcion == "3":
            informacion_usuario()
        elif opcion == "4":
            valores_unicos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
