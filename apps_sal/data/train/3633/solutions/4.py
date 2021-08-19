def shuffle_it(xs, *nss):
    for (i, j) in nss:
        (xs[i], xs[j]) = (xs[j], xs[i])
    return xs
