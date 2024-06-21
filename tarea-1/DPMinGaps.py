def min_gaps_squared(L, S):
    n = len(S)
    # dp[i] guarda la suma mínima de espacios al cuadrado 
    dp = [float('inf')] * (n + 1)
    # dp se inicializa en infinito para ir minimizando su valor, si dp[0]=0, entonces no hay gaps
    dp[0] = 0
    
    # itera sobre cada ladrillo
    for i in range(1, n + 1):
        current_length = 0 
        # itera desde el ladrillo actual hasta el primero

        # al comenzar desde el ladrillo i y movernos hacia atrás, intentamos ver cuántos ladrillos podemos agregar 
        # a la fila actual antes de que la longitud total exceda L
        for j in range(i, 0, -1):
            current_length += S[j-1]
            if current_length > L:
                break
            remaining_space = L - current_length
            # espacios al cuadrado
            gap_squared = remaining_space ** 2
            # selecciona entre el mínimo de gaps actual y la suma de gaps hasta el ladrillo j-1 y le suma gap_squared
            dp[i] = min(dp[i], dp[j-1] + gap_squared)
    
    return dp[n]

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
        print(min_gaps_squared(L, S))

    except EOFError:
        break