def zeros(n):
    return sum([n//5**i for i in range(1, len(str(n)) + len(str((n//1000) + 1))) ])
