from collections import Counter


def around_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    s = str(a)
    c = Counter(s)
    max_d = [0, None]
    for d in '0123456789':
        if c[d] > max_d[0]:
            max_d = [c[d], d]
    chunks = [s[i:i + 25] for i in range(0, len(s), 25)]
    return 'Last chunk {}; Max is {} for digit {}'.format(chunks[-1], max_d[0], max_d[1])
