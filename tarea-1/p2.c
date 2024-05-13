#include <stdio.h>
#include <stdlib.h> // Necesario para usar malloc y free

int main() 
{
    // Longitud de la pared
    int L;

    // Largo de la secuencia S
    int n;

    // Secuencia de longitudes de cada ladrillo
    int *S;

    // Asignar memoria para el arreglo S
    S = (int*)malloc(n * sizeof(int));
    
    if (S == NULL) {
        printf("Error: No se pudo asignar memoria.\n");
        return 1;
    }

    // Ejecutar algoritmo

    // Liberar la memoria asignada para el arreglo S
    free(S);

    return 0;
}
