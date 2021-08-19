from functools import reduce


def list_squared(m, n):
    answer = []
    for i in range(m, n + 1):
        root = sumSquares(factors(i)) ** 0.5
        if root == round(root):
            answer.append([i, int(root ** 2)])
    return answer


def factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def sumSquares(l):
    return sum((i ** 2 for i in l))
