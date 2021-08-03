from functools import reduce


def sum_for_list(lst):
    factors = []
    for j in lst:
        for k in [i for i in range(2, abs(j) + 1) if j % i == 0]:
            if factors == [] or reduce(lambda x, y: x and y, [k % m != 0 for m in factors]):
                factors.append(k)
    return [[j, sum([l for l in lst if l % j == 0])] for j in sorted(factors)]
