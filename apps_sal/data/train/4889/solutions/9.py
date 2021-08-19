def fila_left(n, fila):
    """Asigna al array con las filas de la grid el array de filas a la izqda"""
    output = [None] * (2 * n - 1)
    column = 0
    while column <= n - 1:
        output[column] = [fila[row][0] for row in range(n + column)]
        for row in range(n + column):
            fila[row].pop(0)
        column += 1
    while column <= 2 * n - 2:
        output[column] = [fila[row][0] for row in range(column - n + 1, 2 * n - 1)]
        for row in range(column - n + 1, 2 * n - 1):
            fila[row].pop(0)
        column += 1
    return output


def max_hexagon_beam(n: int, seq: tuple):
    celdas = 3 * n ** 2 - 3 * n + 1
    elementos = [n + i for i in range(n)] + [2 * n - 2 - i for i in range(n - 1)]
    filas = len(elementos)
    grid = []
    for i in range(celdas):
        grid.append(seq[i % len(seq)])
    # Analizamos filas
    fila = [None] * filas
    usados = 0
    for i in range(filas):
        fila[i] = grid[usados:usados + elementos[i]]
        usados += elementos[i]
    maximo = max(sum(fila[i]) for i in range(filas))

    # Analizamos filas a la izquierda por dos veces
    fila2 = fila_left(n, fila)
    fila2 = [row[::-1] for row in fila2]
    maximo_left = max(sum(fila2[i]) for i in range(filas))
    fila3 = fila_left(n, fila2)
    fila3 = [row[::-1] for row in fila3]
    maximo_right = max(sum(fila3[i]) for i in range(filas))
    return max(maximo, maximo_left, maximo_right)
