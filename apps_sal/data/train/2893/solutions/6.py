def plant_doubling(n):
    schemat = str(bin(n))
    return sum((int(schemat[i]) for i in range(2, len(schemat))))
