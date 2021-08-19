import heapq


def closure_gen(*s):
    if not s:
        raise StopIteration()
    h = set(s)
    q = list(h)
    heapq.heapify(q)
    if q == [1]:
        yield 1
        raise StopIteration()
    while True:
        x = heapq.heappop(q)
        h.remove(x)
        yield x
        for y in s:
            z = x * y
            if y != 1 and z not in h:
                heapq.heappush(q, z)
                h.add(z)
