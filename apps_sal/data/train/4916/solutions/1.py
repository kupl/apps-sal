primes = [2, 3, 5, 7, 11]


def gen_primes():
    yield from primes
    candidate = primes[-1]
    candidate_root = int(candidate ** 0.5) + 1
    while True:
        candidate += 2
        if candidate_root * candidate_root < candidate:
            candidate_root += 1
        for p in primes:
            if candidate % p == 0:
                break
            if p > candidate_root:
                primes.append(candidate)
                yield candidate
                break


def get_primes(how_many, group_size=2):
    result = []
    for i, p in enumerate(gen_primes(), start=1):
        result.append(p)
        if len(result) == group_size:
            yield tuple(result)
            result = []
        if i == how_many:
            break
    if len(result) > 0:
        while len(result) < group_size:
            result.append(None)
        yield tuple(result)
