from collections import Counter


def f(n):
    i = 3
    sum = 1
    lists = []
    while (n / 2).is_integer():
        lists.append(2)
        n //= 2
    while n != 1 and i <= n:

        while n % i == 0:
            lists.append(i)
            n //= i

        i += 2
    for i in dict(Counter(lists)):
        a = dict(Counter(lists))[i]
        sum *= (a * (i ** (a - 1)))
    return sum
