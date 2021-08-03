from collections import deque


def custom_fib(signature, indexes, n):
    fib = deque(signature)
    for _ in range(n):
        fib.append(sum(map(fib.__getitem__, indexes)))
        fib.popleft()
    return fib[0]
