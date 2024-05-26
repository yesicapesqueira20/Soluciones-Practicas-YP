#usando bucle While
# Solicitar al usuario que ingrese un número entero entre 1 y 10
numero = int(input("Ingrese un número entero entre 1 y 10: "))

# Asegurarse de que el número esté dentro del rango válido
while numero < 1 or numero > 10:
    print("El número ingresado no está en el rango entre 1 y 10.")
    numero = int(input("Ingrese un número entero entre 1 y 10: "))

# Inicializar el contador
i = 1

# Generar la tabla de multiplicar usando while
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1

#usando bucle for
# Solicitar al usuario que ingrese un número entero entre 1 y 10
numero = int(input("Ingrese un número entero entre 1 y 10: "))

# Asegurarse de que el número esté dentro del rango válido
while numero < 1 or numero > 10:
    print("El número ingresado no está en el rango entre 1 y 10.")
    numero = int(input("Ingrese un número entero entre 1 y 10: "))

# Generar la tabla de multiplicar usando for
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

