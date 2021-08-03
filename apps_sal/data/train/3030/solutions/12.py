def nb_dig(n, d):
    square_list = [str(k**2) for k in range(0, n + 1)]
    result = 0
    result = "".join(square_list).count(str(d))
    return result
