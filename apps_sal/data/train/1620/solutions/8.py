import heapq


def n_linear_generator(m):
    u = [1]
    s = set(u)
    while True:
        x = heapq.heappop(u)
        yield x
        s.remove(x)
        for y in m:
            z = x * y + 1
            if z not in s:
                heapq.heappush(u, z)
                s.add(z)


memos = {}


def n_linear(m, n):
    m = tuple(m)
    if m not in memos:
        memos[m] = ([], n_linear_generator(m))
    (past, gen) = memos[m]
    past.extend((next(gen) for _ in range(len(past), n + 1)))
    return past[n]
