def find(n):
    m = 0
    for i in range(1, n + 1):
        if i % 3 is 0 or i % 5 is 0:
            m = m + i
    return m
