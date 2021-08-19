def largest_sum(arr):
    (c, m) = (0, 0)
    for n in arr:
        c = max(0, c + n)
        m = max(m, c)
    return m
