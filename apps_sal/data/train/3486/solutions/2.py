from collections import deque

def person(n, m):
    q = deque(range(n))
    for i in range(n):
        q.rotate(1-m)
        x = q.popleft()
    return x + 1

def coins(n, m):
    return sum(m + max(i-m, 0) * 2 for i in range(n, 1, -1))

def find_last(n, m):
    return person(n, m), coins(n, m)
