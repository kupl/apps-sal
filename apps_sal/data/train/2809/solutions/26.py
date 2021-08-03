def digitize(n):
    n = str(n)
    n_list = list(map(int, str(n)))
    n_list.reverse()
    return n_list
