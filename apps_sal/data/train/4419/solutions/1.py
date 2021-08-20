def reg_sum_hits(n, s):
    return sorted(map(list, __import__('collections').Counter(map(sum, __import__('itertools').product(range(1, s + 1), repeat=n))).items()))
