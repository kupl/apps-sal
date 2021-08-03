from heapq import heappush, heappop, heapify


def closure_gen(*s):
    if not s:
        return None
    set_s = set(s)
    heap_s = [i for i in s]
    heapify(heap_s)
    while set_s:
        current = heappop(heap_s)
        new_values = {current * i for i in s}.difference(set_s)
        for i in new_values:
            heappush(heap_s, i)
        set_s.update(new_values)
        set_s.discard(current)
        yield current
