def find(n):
    L = []
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            L.append(i)
    return sum(L)
