def find(n):
    return sum(filter(lambda i: (i % 5 == 0) or (i % 3 == 0), range(n + 1)))
