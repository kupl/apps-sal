def count_subsequences(needle, haystack):
    count = [1] + [0] * len(needle)
    for a in haystack:
        count = [1] + [count[i] + count[i - 1] * (a == b)
                       for i, b in enumerate(needle, 1)]
    return count[-1] % 10 ** 8
