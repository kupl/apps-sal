def collatz_step(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1


def collatz_seq(n):
    while n != 1:
        yield n
        n = collatz_step(n)
    yield 1


def collatz(n):
    return '->'.join((str(x) for x in collatz_seq(n)))
