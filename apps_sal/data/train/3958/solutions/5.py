from collections import deque


def custom_fib(signature, indexes, n):
    s = deque(signature, maxlen=len(signature))
    for i in range(n):
        s.append(sum((s[i] for i in indexes)))
    return s[0]
