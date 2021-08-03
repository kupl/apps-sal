from collections import Counter
from itertools import permutations
from itertools import chain
import numpy as np


def prime_factors(n):
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)

    for k in range(3, n + 1, 2):
        while n % k == 0:
            n = n // k
            factors.append(k)
        if n == 1:
            break
    return factors


def get_score(factors):
    factor_counts = Counter(factors)
    return sum(f**factor_counts[f] for f in factor_counts) * sum(c for c in factor_counts.values())


def int_partitions(m, memo={}):
    if m in memo:
        return memo[m]
    all_partitions = [[m]]

    for i in range(1, m):
        for p in int_partitions(m - i, memo):
            all_partitions.append([i] + p)

    memo[m] = all_partitions
    return all_partitions


def make_partitions(factors):
    partitions = int_partitions(len(factors))
    part_perm = []

    for p in partitions:
        part_perm.append(set(list(permutations(p, len(p)))))

    part_perm = set(list(chain.from_iterable(part_perm)))
    all_new_factors = []

    for inds in part_perm:
        new_factors = []
        j_start = 0

        for i in inds:
            j_end = j_start + i
            new_factors.append(np.product(factors[j_start:j_end]))
            j_start = j_end

        if len(new_factors) > 1:
            all_new_factors.append(new_factors)

    return all_new_factors


def find_spec_prod_part(n, com):
    factors = prime_factors(n)

    if len(factors) == 1:
        return "It is a prime number"

    all_factors = make_partitions(factors)
    scores = [get_score(x) for x in all_factors]

    if com == "max":
        opt_id = np.argmax(scores)
    else:
        opt_id = np.argmin(scores)

    return [sorted(all_factors[opt_id], reverse=True), scores[opt_id]]
