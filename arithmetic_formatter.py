def arithmetic_arranger(problemas, solucion=False):  # Cambié solucion a False para alinearse con el problema original
    if len(problemas) > 5:
        return "Error: Demasiados problemas."

    # Inicializar las listas que contendrán las líneas formateadas
    linea1, linea2, linea3, linea4 = [], [], [], []

    for problema in problemas:
        partes = problema.split()  # Divide cada problema en sus componentes
        num1, operador, num2 = partes[0], partes[1], partes[2]

        # Validaciones
        if operador not in ['+', '-']:
            return "Error: Operador debe ser '+' o '-'."
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Los numeros solo pueden contener digitos.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Los numeros no pueden tener mas de 4 digitos.'

        # Calcular el ancho del problema
        ancho = max(len(num1), len(num2)) + 2

        # Formatear cada línea
        primera_linea = num1.rjust(ancho)
        segunda_linea = operador + ' ' + num2.rjust(ancho - 2)
        tercera_linea = '-' * ancho

        # Si se pide mostrar las respuestas
        if solucion:
            if operador == '+':
                resultado = str(int(num1) + int(num2))
            else:
                resultado = str(int(num1) - int(num2))
            cuarta_linea = resultado.rjust(ancho)

        # Añadir las líneas a las listas correspondientes
        linea1.append(primera_linea)
        linea2.append(segunda_linea)
        linea3.append(tercera_linea)
        if solucion:
            linea4.append(cuarta_linea)

    # Unir las líneas con cuatro espacios de separación
    array_problemas = '    '.join(linea1) + '\n' + '    '.join(linea2) + '\n' + '    '.join(linea3)
    
    if solucion:
        array_problemas += '\n' + '    '.join(linea4)

    return array_problemas

# Ejemplo de uso
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))