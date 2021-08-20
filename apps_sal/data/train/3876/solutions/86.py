def find(n):
    return sum(filter(is_multiple_of_3_or_5, range(n + 1)))


def is_multiple_of_3_or_5(n):
    return n % 3 == 0 or n % 5 == 0
