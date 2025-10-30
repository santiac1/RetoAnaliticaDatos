def leer_csv_a_matriz(nombre_archivo):
    matriz = []
    f = open(nombre_archivo, "r", encoding="utf-8")  # open
    for linea in f:                                   # for-linea-archivo
        linea = linea.rstrip("\n")                    # rstrip
        fila = linea.split(",")                       # split por coma (según guía)
        matriz.append(fila)
    f.close()                                         # close
    return matriz

def main():
    datos = leer_csv_a_matriz("titanic.csv")
    # datos[0] = encabezados
    print("Encabezados:")
    print(datos[0])

    print("Primera línea:")
    print(datos[1])

    # Preguntas pedidas:
    objetos = len(datos) - 1          # sin contar encabezado
    variables = len(datos[0])         # número de columnas
    valor_var2_obj4 = datos[4][1]     # objeto 4 => índice 4; variable 2 => índice 1

    print("¿Cuántos objetos hay?:", objetos)
    print("¿Cuántas variables hay?:", variables)
    print("¿Cuál es el valor de la variable 2 del objeto 4?:", valor_var2_obj4)

if _name_ == "_main_":
    main()
PY
