from itertools import count


def collatz(n):
    for iteration in count(1):
        if n == 1:
            return iteration
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
