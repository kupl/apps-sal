from collections import deque


def sort_array(a):
    asc = deque(sorted(x for x in a if x % 2))
    desc = sorted(x for x in a if not x % 2)
    return [asc.popleft() if x % 2 else desc.pop() for x in a]
