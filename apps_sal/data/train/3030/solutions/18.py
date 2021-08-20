def nb_dig(n, d):

    def ds_in_k(k):
        (m, r) = divmod(k, 10)
        return int(r == d) + (ds_in_k(m) if m else 0)
    return sum((ds_in_k(k ** 2) for k in range(n + 1)))
