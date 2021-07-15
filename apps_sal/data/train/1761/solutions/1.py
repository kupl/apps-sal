cache = [0, 2, 4]
comp = [0, 2, 6]

repeat = len(cache)-1
b = cache[-1]
while comp[-1] < 2 ** 41:
    if len(cache) >= b:
        repeat += 1
        b = cache[repeat]
    cache.append(cache[-1] + repeat)
    comp.append(comp[-1] + (cache[-1] - cache[-2]) * (len(cache) - 1))

from bisect import bisect
def find(n):
    repeat = bisect(comp, n)
    return cache[repeat-1] + (n - comp[repeat-1]) // repeat
