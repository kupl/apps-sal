from itertools import chain

CACHE, INF = {}, float('inf')
lst = list(chain.from_iterable(('', d) for d in '123456789'))[1:]


def dfs(i=1, nOps=0):
    if i == 17:
        v = eval(''.join(lst))
        if nOps < CACHE.get(v, INF):
            CACHE[v] = nOps
    else:
        for o in ('', '+', '-'):
            lst[i] = o
            dfs(i + 2, nOps + bool(o))


dfs()

operator_insertor = CACHE.get
