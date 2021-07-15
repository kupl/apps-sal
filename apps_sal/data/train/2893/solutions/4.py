def plant_doubling(n):
    return sum(c == '1' for c in bin(n)[2:])
