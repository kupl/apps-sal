
def count_red_beads(n):
    lista = []
    if n < 2:
        return 0
    for i in range(1, n):
        lista.append(i * 2)
    return lista[-1]
