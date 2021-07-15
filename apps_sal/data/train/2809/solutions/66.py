def digitize(n):
    list_n = list(str(n))
    list_n.reverse()
    return list(map(int, list_n))
