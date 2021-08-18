from collections import defaultdict


def sum_for_list(lst):

    primes = [2, ]
    factors_dict = defaultdict(list)
    answer = []

    x = 3
    for num in range(max(abs(i) for i in lst)):
        if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
            primes += [x]
        x += 2

    for k in primes:
        factors_dict[k]

    for prime in primes:
        for i in lst:
            if i % prime == 0:
                factors_dict[prime] += [i]

    for k, v in list(factors_dict.items()):
        if v:
            answer += [[k, sum(v)]]

    return answer
