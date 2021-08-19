def find(seq):
    (a, b, n) = (min(*seq), max(*seq), len(seq))
    m = (b - a) // n
    return m * abs(sum(((x - a) // m for x in seq)) - (n + 1) * n // 2) + a
