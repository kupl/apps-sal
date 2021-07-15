def _prime_factors(n):
    factors = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors.keys():
                factors[i] += 1
            else:
                factors[i] = 1
    if n > 1:
        if n in factors.keys():
            factors[n] += 1
        else:
            factors[n] = 1

    return factors


def chain_arith_deriv(start, m, chain=None):
    factors = _prime_factors(start)
    if len(factors) == 1 and chain is None:
        return '{} is a prime number'.format(start)
    if chain is None:
        chain = []
    chain.append(start)

    if m == 1:
        return chain
    elif start == 1:
        next_num = 1
    else:
        next_num = 0
        for p, k in factors.items():
            next_num += k/p*start
    return chain_arith_deriv(round(next_num), m-1, chain=chain)
