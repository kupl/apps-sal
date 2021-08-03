from functools import reduce


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def list_squared(m, n):
    ans = []

    for i in range(m, n):
        factor_sum = 0
        factor_ans = []

        for j in factors(i):
            factor_sum += j**2

        if (factor_sum**0.5).is_integer():
            factor_ans.append(i)
            factor_ans.append(factor_sum)
            ans.append(factor_ans)
    return ans
