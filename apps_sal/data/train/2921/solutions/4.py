L = ["gold", "diamond", "emerald", "iron"]


def blocks_to_collect(level):
    D = {"total": 0, "gold": 0, "diamond": 0, "emerald": 0, "iron": 0}
    for i, x in enumerate(range(3, 2 * level + 2, 2)):
        D[L[i % 4]] += x**2
    D["total"] = level + 4 * level * (level + 1) * (level + 2) // 3
    return D
