def find_primes_sextuplet(limit):
    for p in [7, 97, 16057, 19417, 43777, 1091257, 1615837, 1954357, 2822707, 2839927, 3243337, 3400207, 6005887]:
        if p * 6 + 48 > limit:
            return [p, p + 4, p + 6, p + 10, p + 12, p + 16]
