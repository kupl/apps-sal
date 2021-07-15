cache = [0, 2, 4]
pc = [0, 2, 6]

repeat = len(cache)-1
b = cache[-1]
while pc[-1] < 2 ** 41:
    if len(cache) >= b:
        repeat += 1
        b = cache[repeat]
    cache.append(cache[-1] + repeat)
    pc.append(pc[-1] + (cache[-1] - cache[-2]) * (len(cache) - 1))

from bisect import bisect
def find(n):
    repeat = bisect(pc, n)
    return cache[repeat-1] + (n - pc[repeat-1]) // repeat
