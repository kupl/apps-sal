def max_collatz_length(n):
    if type(n) != int or n <= 0:
        return []
    lengths = {1: 1}
    for i in range(2, n + 1):
        a = [i]
        while a[-1] not in lengths:
            a += [3 * a[-1] + 1] if a[-1] % 2 else [a[-1] // 2]
        for (j, k) in enumerate(a[::-1]):
            lengths[k] = j + lengths[a[-1]]
    return [max(lengths, key=lengths.get), lengths[max(lengths, key=lengths.get)]]
