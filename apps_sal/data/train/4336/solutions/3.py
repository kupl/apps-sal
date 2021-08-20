from operator import itemgetter


def mem_alloc(banks):
    cache = set()
    count = 0
    while tuple(banks) not in cache:
        cache.add(tuple(banks))
        count += 1
        (ind, val) = max(enumerate(banks), key=itemgetter(1))
        banks[ind] = 0
        for i in range(val):
            ind += 1
            banks[ind % len(banks)] += 1
    return count
