from collections import deque

def reverse(lst):
    q = deque()
    for x in lst:
        q.appendleft(x)
    return list(q)
