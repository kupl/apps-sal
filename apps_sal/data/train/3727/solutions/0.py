def pythagorean_triplet(n):
    for a in range(3, n):
        for b in range(a + 1, n):
            c = (a * a + b * b)**0.5
            if a * b * c > n:
                break
            if c == int(c) and a * b * c == n:
                return [a, b, c]
