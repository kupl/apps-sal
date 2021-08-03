import heapq


def closure_gen(*s):
    s = set(sorted(s))
    buf = list(s)
    heapq.heapify(buf)
    while True:
        if len(buf) == 0:
            raise StopIteration
        val = heapq.heappop(buf)
        while len(buf) > 0 and buf[0] == val:
            heapq.heappop(buf)
        for v in s:
            if v <= 1:
                continue
            heapq.heappush(buf, val * v)
        yield val
