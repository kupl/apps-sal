def faro_cycles(n):
    original = list(range(1, n + 1))
    duplicate, c = original.copy(), 0
    while 1:
        first, bottom = duplicate[0], duplicate[-1]
        first_half = duplicate[1:n // 2]
        second_half = duplicate[n // 2:-1]
        duplicate = []
        for i, j in zip(first_half, second_half):
            duplicate.extend([j, i])
        duplicate = [first] + duplicate + [bottom]
        c += 1
        if original == duplicate:
            return c
