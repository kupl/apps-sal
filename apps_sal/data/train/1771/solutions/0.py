from heapq import heappush, heappop


def closure_gen(*s):
    q = sorted(s)
    m = set(s)
    while q:
        curr = heappop(q)
        yield curr
        for i in s:
            t = curr * i
            if t not in m:
                heappush(q, t)
                m.add(t)
