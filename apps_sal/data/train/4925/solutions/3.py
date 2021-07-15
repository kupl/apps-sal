def _collatz(n):
    yield n
    while n != 1:
        n = (n // 2, 3 * n + 1)[n % 2]
        yield n

def collatz(n):
    return '->'.join(map(str, _collatz(n)))
