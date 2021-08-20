def binRota(arr):
    rota = []
    for (i, row) in enumerate(arr):
        if i % 2:
            row = reversed(row)
        rota.extend(row)
    return rota
