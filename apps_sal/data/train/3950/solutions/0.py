def score(sub_gen): return lambda n: sum(int(''.join(sub)) for length in range(1, len(str(n)) + 1) for sub in sub_gen(str(n), length))


score1 = score(__import__('itertools').combinations)
score2 = score(lambda s, r: (s[i: i + r] for i in range(len(s) - r + 1)))


def divs(n): return set.union(*({d, n // d} for d in range(1, int(n ** .5) + 1) if not n % d)) - {1, n}


def find_int_inrange(a, b):
    div_range = [0]
    for n in range(a, b + 1):
        common_divisors = divs(score1(n)) & divs(score2(n))
        if len(common_divisors) > div_range[0]:
            div_range = [len(common_divisors)]
        if len(common_divisors) == div_range[0]:
            div_range.append(n)
    return div_range
