def solve(lst):
    return sorted(lst, key=factors_count)


def factors_count(n):
    result = []
    for k in (2, 3):
        while n % k == 0:
            n //= k
            result.append(k)
    return -result.count(3), result.count(2)
