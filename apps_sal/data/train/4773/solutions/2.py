from functools import reduce
from collections import deque


def count_find_num(primesL, limit):
    q = deque()
    q.append(reduce(lambda x, y: x * y, primesL))
    Max, Count = 0, 0
    while len(q) != 0:
        if q[0] <= limit:
            Count += 1
            Max = max(Max, q[0])
            for i in primesL:
                if i * q[0] <= limit and i * q[0] not in q:
                    q.append(i * q[0])
        q.popleft()
    return [Count, Max] if Count != 0 and Max != 0 else []
