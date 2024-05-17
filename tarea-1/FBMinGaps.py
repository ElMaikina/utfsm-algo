
# Obtiene recursivamente todas las combinaciones de ladrillos
#def combinatoria(S):
#    if S:
#        result = combinatoria(S[:-1])
#        return result + [c + [S[-1]] for c in result]
#    else:
#        return [[]]

def min_gaps_rec(L, S, s):
    # la suma de los gaps totales
    gaps = 0

    # largo total de los ladrillos dispuestos
    current_length = 0

    # cada rama generara un resultado, los cuales se 
    # guardan aqui para luego extraer el menor resultado
    results = []

    for brick in S:
        new_array = S
        new_array.remove(brick)
        new_array.append(brick)

        results.append(min_gaps_rec(L, new_array, level+1))

        # Calcula los gaps para el arreglo de ladrillos
        if (current_length + int(brick) < L):
            current_length += int(brick)

        if (current_length + int(brick) >= L):
            gaps = (L - current_length)**2
            current_length = 0

    # Esta seccion calcula los gaps
    results.append(gaps)

    return min(results)

while True:
    try:
        # Leer la línea de entrada
        line = input()
        # Dividir la línea en valores enteros
        values = list(map(int, line.split()))
        # Obtener el tamaño de L
        L = values[0]

        # Leer la siguiente línea de entrada
        line = input()
        # Dividir la línea en valores enteros
        values = list(map(int, line.split()))
        # Obtener la lista de tamaños de los ladrillos
        S = values[:]

        # Imprimir el resultado
        print(min_gaps_rec(L, S, 0))

    except EOFError:
        break