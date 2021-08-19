def nb_dig(n, d):
    d_count = []
    for n in range(n + 1):
        square = str(n ** 2)
        d_count.append(square.count(str(d)))
    return sum(d_count)
