import numpy as np
import random


def generar_matriz_adyacencia(n_vertices):
    matriz = np.zeros((n_vertices, n_vertices), dtype=int)
    for i in range(n_vertices):
        grado_aleatorio = random.randint(0, n_vertices - 1)
        vertices_adyacentes = random.choices(
            range(n_vertices), k=grado_aleatorio)
        for j in vertices_adyacentes:
            if i != j:
                matriz[i][j] = 1

        matriz[i][i] = random.randint(0, 1)

    return matriz


def contar_aristas_lazos_grado(matriz):
    n_vertices = len(matriz)
    aristas = 0
    lazos = 0
    grado_por_vertice = [0] * n_vertices

    for i in range(n_vertices):
        for j in range(n_vertices):
            if matriz[i][j] == 1:
                if i == j:
                    lazos += 1
                else:
                    aristas += 1
            grado_por_vertice[i] += matriz[i][j]
    return aristas, lazos, grado_por_vertice


def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(valor) for valor in fila))


def main():
    n_vertices = 6
    matriz_adyacencia = generar_matriz_adyacencia(n_vertices)

    print("Matriz de adyacencia:")
    imprimir_matriz(matriz_adyacencia)

    num_aristas, num_lazos, grado_por_vertice = contar_aristas_lazos_grado(
        matriz_adyacencia)
    result = num_lazos+num_aristas
    print(f"Numero de aristas: {result}")
    print(f"Numero de lazos: {num_lazos}")
    print(f"Grado de cada vertice:")
    for vertice, grado in enumerate(grado_por_vertice):
        print(f"Vertice {vertice + 1}: {grado}")


if __name__ == "__main__":
    main()
