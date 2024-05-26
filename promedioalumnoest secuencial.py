# Solicitar al usuario que ingrese las notas de las 5 materias
nota1 = float(input("Ingrese la nota de la materia 1: "))
nota2 = float(input("Ingrese la nota de la materia 2: "))
nota3 = float(input("Ingrese la nota de la materia 3: "))
nota4 = float(input("Ingrese la nota de la materia 4: "))
nota5 = float(input("Ingrese la nota de la materia 5: "))

# Calcular la suma de las notas
suma = nota1 + nota2 + nota3 + nota4 + nota5

# Calcular el promedio
promedio = suma / 5

# Mostrar el promedio
print("El promedio de las notas es:", promedio)
