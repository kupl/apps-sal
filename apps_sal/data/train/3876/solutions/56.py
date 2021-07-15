def find(n):
    return sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, list(range(1, n + 1)))))
