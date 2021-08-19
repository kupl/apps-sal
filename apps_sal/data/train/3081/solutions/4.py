import random


def squares(n):
    return [x ** 2 for x in range(1, n + 1)]


def num_range(n, start, step):
    list = []
    for i in range(n):
        list.append(start)
        start += step
    return list


def rand_range(n, mn, mx):
    return [random.randint(mn, mx) for x in range(n)]


def primes(n):
    list = []
    num = 2
    while len(list) != n:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            list.append(num)
        num += 1
    return list
