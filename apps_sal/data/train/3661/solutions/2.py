from collections import defaultdict

def partitions(n, I=1):
    yield (n, [n])
    for i in range(n//2, I-1, -1):
        for x,p in partitions(n-i, i):
            yield (x*i, p+[i])

def find_part_max_prod(n):
    result = defaultdict(list)
    for x,p in partitions(n):
        result[x].append(p)
    k, v = max(result.items())
    return [*v, k]
