from itertools import combinations

def min_gaps_squared_brute_force(L, S):

    # Calcula los gaps para el arreglo de ladrillos
    def calculate_gaps(parts):
        total_gap_squared = 0
        # Suma ladrillo por ladrillo hasta ser mas largo que el maximo
        for part in parts:
            length_sum = sum(part)
            if length_sum <= L:
                gap = L - length_sum
                # Se suma la diferencia al cuadrado
                total_gap_squared += gap ** 2
            else:
                return float('inf')  # Invalid partition
        return total_gap_squared

    # Genera las particiones con los ladrillos dispuestos
    def generate_combinations(arr):
        if len(arr) == 1:
            return [[arr]]
        
        result = []
        for i in range(1, len(arr) + 1):
            for c in combinations(range(1, len(arr)), i-1):
                start = 0
                partition = []
                for end in c:
                    partition.append(arr[start:end])
                    start = end
                partition.append(arr[start:])
                result.append(partition)
        return result

    partitions = generate_combinations(S)
    min_gap_squared = float('inf')

    # Llama recursivamente a la funcion para generar todos los ordenes
    for parts in partitions:
        gap_squared = calculate_gaps(parts)
        min_gap_squared = min(min_gap_squared, gap_squared)

    return min_gap_squared

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
        print(min_gaps_squared_brute_force(L, S))

    except EOFError:
        break
