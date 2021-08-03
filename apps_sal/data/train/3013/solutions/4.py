from itertools import combinations


def delete_digit(n):
    return max(int(''.join(i)) for i in list(combinations(str(n), len(str(n)) - 1)))
