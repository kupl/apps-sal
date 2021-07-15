def mystery(n):
    if n < 1:
        return []
    d = {1, n}
    for k in range(2, int(n ** 0.5) + 1):
        if not n % k:
            d.add(k)
            d.add(n // k)
    return sorted(i for i in d if i % 2)

