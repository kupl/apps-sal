def get_primes(how_many, group_size):
    primes = [False] * 2 + list(range(2, 13 * how_many))
    for x in primes:
        if x:
            for i in range(x * x, 13 * how_many, x):
                primes[i] = False
    seq = sorted(set(primes))[1:how_many + 1]
    while len(seq) % group_size != 0:
        seq += [None]
    return (tuple(seq[x:x + group_size]) for x in range(0, len(seq), group_size))
