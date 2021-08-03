def mem_alloc(banks):
    banks, memo, size = tuple(banks), set(), len(banks)
    while banks not in memo:
        memo.add(banks)
        i = max(range(size), key=banks.__getitem__)
        q, r = divmod(banks[i], size)
        x, y = r + i, r + i - size
        banks = tuple(q if i == j else banks[j] + q + (i < j <= x or j <= y) for j in range(size))
    return len(memo)
