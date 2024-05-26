# Precio por unidad de leche
precio_unidad = 1000

# Solicitar al usuario la cantidad de unidades compradas
cantidad = int(input("Ingrese la cantidad de unidades compradas: "))

# Solicitar al usuario si es jubilado
es_jubilado = input("¿Es usted jubilado? (sí/no): ").strip().lower()

# Calcular el costo total sin descuentos
costo_total = cantidad * precio_unidad

# Inicializar descuento
descuento = 0

# Determinar el descuento según la cantidad comprada
if cantidad > 24:
    descuento = 0.15
elif cantidad > 12:
    descuento = 0.10

# Añadir el descuento por ser jubilado
if es_jubilado == "sí":
    descuento += 0.10

# Calcular el total de descuento
total_descuento = costo_total * descuento

# Calcular el costo total con descuento
costo_total_con_descuento = costo_total - total_descuento

# Mostrar el costo total
print("El costo total con descuento es:", costo_total_con_descuento)
