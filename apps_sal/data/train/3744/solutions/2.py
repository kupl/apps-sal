from collections import defaultdict


def oddity(n):
    if n == -1:
        return float('inf')
    odd = 0
    while n % 2:
        odd += 1
        n //= 2
    return odd


def oddest(a):
    result = defaultdict(list)
    for n in a:
        result[oddity(n)].append(n)
    try:
        x, = result[max(result)]
        return x
    except ValueError:
        pass
