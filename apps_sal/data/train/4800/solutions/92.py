def collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


def hotpo(n):
    i = 0
    while n != 1:
        n = collatz(n)
        i += 1
    return i
