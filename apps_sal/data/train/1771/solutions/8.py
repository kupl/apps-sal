def closure_gen(*s):
    s = [*s]

    if 1 in s:
        s.remove(1)
        yield 1

    queue = [(n, n, 0) for n in s]
    numbers = [1]

    while queue:
        prod, *_ = min(queue)
        yield prod

        numbers.append(prod)
        for i, (p, n, d) in enumerate(queue):
            if p <= prod:
                d += p == prod
                queue[i] = numbers[d] * n, n, d
