def cycle(n):
    if not n % 2 or not n % 5:
        return -1
    (m, s) = (1, set())
    while m not in s:
        s.add(m)
        m = 10 * m % n
    return len(s)
