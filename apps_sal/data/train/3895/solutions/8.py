from collections import deque

def shifted_diff(f, s):
    d1, d2 = deque(f), deque(s)
    l = [d2.rotate(-1) or d1 == d2 for i in range(len(f))]
    return (l.index(True) + 1) % len(l) if True in l else -1

