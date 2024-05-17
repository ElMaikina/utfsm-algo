# La idea de este algoritmo recursivo es generear todas las
# posibles combinaciones de ladrillos y recursivamente obtener
# el menor valor desde los nodos finales

# El algoritmo ira vaciando el arreglo S de ladrillos y generara
# las combinaciones en la variable Pila

# Una vez se llega al nodo final (osea que S se vacia completamente)
# el algoritmo calculara el valor de los gaps generados y lo retornara
# hacia los nodos que lo preceden

def min_gaps_rec(L, S, pila):
    # Largo del arreglo de ladrillos
    n = len(S)
    # la suma de los gaps totales
    gaps = 0
    # largo total de los ladrillos dispuestos
    current_length = 0
    # Arreglo de resultados obtenidos
    results = []

    # Calcula los gaps para el arreglo de ladrillos

    # La ultima hoja generada por el arbol se encarga
    # de calcular las gaps del orden generado
    if (len(S) == 0):
        for e in pila:
            if (current_length + int(e) < L):
                current_length += int(e)
            if (current_length + int(e) >= L):
                gaps += (L - current_length)**2
                current_length = 0
        
        return gaps

    # Los nodos del arbol generan todas las combinaciones
    # posibles al mover los elementos de S hacia la Pila
    if (len(S) > 0):
        for i in range(0, n):
            brick = S[i]
            new_s = S.copy()
            new_s.pop(i)
            new_pila = pila.copy()
            new_pila.append(brick)
            result = min_gaps_rec(L, new_s, new_pila)        
            results.append(result)
    
    if (len(pila) == 0):
        print('Resultado: ' + str(min(results)))
    
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
        min_gaps_rec(L, S, [])

    except EOFError:
        break