from collections import deque

def buy_newspaper(s1,s2):
    if set(s2) - set(s1):
        return -1
    q = deque(s1)
    n = 0
    for c in s2:
        i = q.index(c)
        n += i + 1
        q.rotate(-i-1)
    return n // len(s1) + (n % len(s1) > 0)

