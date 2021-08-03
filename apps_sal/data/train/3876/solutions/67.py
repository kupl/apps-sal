def find(n):
    return sum(filter(IsMultiple, range(n + 1)))


def IsMultiple(n):
    return n % 3 == 0 or n % 5 == 0
