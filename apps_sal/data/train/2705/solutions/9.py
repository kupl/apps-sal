def generate_integers(m, n):
    list = []
    for x in m, n:
        while m <= x <= n:
            x = x + 1
            list.append(x - 1)
        return list
