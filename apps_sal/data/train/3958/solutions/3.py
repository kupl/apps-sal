from collections import deque


def custom_fib(sig, ind, n):
    sig = deque(sig)
    while n >= len(sig):
        (s, n) = (sum((sig[x] for x in ind)), n - 1)
        sig.append(s)
        sig.popleft()
    return sig[n]
