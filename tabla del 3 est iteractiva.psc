Algoritmo tabla_del_3
    // Solicitar al usuario que ingrese un n�mero entero entre 1 y 10
    Escribir "Ingrese un n�mero entero entre 1 y 10: "
    Leer numero
    
    // Verificar que el n�mero est� dentro del rango v�lido
    Mientras numero < 1 o numero > 10 Hacer
        Escribir "El n�mero ingresado no est� en el rango entre 1 y 10."
        Escribir "Ingrese un n�mero entero entre 1 y 10: "
        Leer numero
    FinMientras
	
    // Inicializar el contador
    i <- 1
	
    // Generar la tabla de multiplicar usando mientras
    Mientras i <= 10 Hacer
        resultado <- numero * i
        Escribir numero, " x ", i, " = ", resultado
        i <- i + 1
    FinMientras

	
FinAlgoritmo
