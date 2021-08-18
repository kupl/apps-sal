from collections import defaultdict
from heapq import heappop, heappush


def ulam_sequence(u0, u1, n):
    q, seen, lst = [u1], defaultdict(int), [u0]
    seen[u1] = 1

    while len(lst) < n:

        while 1:
            last = heappop(q)
            if seen[last] == 1:
                break

        for v in lst:
            x = v + last
            if x not in seen:
                heappush(q, x)
            seen[x] += 1

        lst.append(last)

    return lst
