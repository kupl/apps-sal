def solve(lst):
    return sorted(lst, key=factors_count)


def factors_count(n):
    result = [0, 0]
    for k in (2, 3):
        while n % k == 0:
            n //= k
            result[k - 2] += (-1) ** k
    return result
