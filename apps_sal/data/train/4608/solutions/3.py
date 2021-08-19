def finance(n):
    # For each n, there are (n + 1) * (n + 2) / 2 cells with values.
    # For each n, the average value for each cell is n.
    # So for each n, the amount financed is n * [(n + 1) * (n + 2) / 2]
    return n * ((n + 1) * (n + 2) / 2)
