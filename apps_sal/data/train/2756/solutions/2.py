def search_permMult(n_max, k):
    return sum(1 for n in range(1, n_max // k) if sorted(str(n)) == sorted(str(n * k)))

    #pairs = 0
    # for n in range(1, n_max // k):
    #    if sorted(str(n)) == sorted(str(n * k)):
    #        pairs = pairs + 1
    # return pairs
