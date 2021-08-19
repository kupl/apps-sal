from itertools import islice


def find_repeat(a, b):
    x = f'{a}{b}'
    seen = {x: 0}
    while True:
        x += str(int(x[-2]) + int(x[-1]))
        last = x[-2:]
        if last in seen:
            i = seen[last]
            return (x[:i], x[i:-2])
        seen[last] = len(x) - 2


def find(a, b, n):
    (prefix, repeat) = [list(map(int, x)) for x in find_repeat(a, b)]
    if n < len(prefix):
        return prefix[n]
    return repeat[(n - len(prefix)) % len(repeat)]
