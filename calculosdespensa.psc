Algoritmo calculosdespensa
    precioUnidad = 1000
	
    // Solicitar al usuario la cantidad de unidades compradas
    Escribir "Ingrese la cantidad de unidades compradas: "
    Leer cantidad
	
    // Solicitar al usuario si es jubilado
    Escribir "¿Es usted jubilado? (True/False): "
    Leer esJubilado
	
    // Calcular el costo total sin descuentos
    costoTotal = cantidad * precioUnidad
	
    // Inicializar descuento
    descuento = 0
	
    // Determinar el descuento según la cantidad comprada
    Si cantidad > 24 Entonces
        descuento = 0.15
	FinSi
	
	Si cantidad > 12 Entonces
        descuento = 0.10
    FinSi
	
    // Añadir el descuento por ser jubilado
    Si esJubilado Entonces
        descuento = descuento + 0.10
    FinSi
	
    // Calcular el total de descuento
    totalDescuento = costoTotal * descuento
	
    // Calcular el costo total con descuento
    costoTotal = costoTotal - totalDescuento
	
    // Mostrar el costo total
    Escribir "El costo total con descuento es: ", costoTotal

	
FinAlgoritmo
