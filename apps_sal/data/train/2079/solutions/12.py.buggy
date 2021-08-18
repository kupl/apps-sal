from functools import lru_cache
from collections import defaultdict
from itertools import tee


price = defaultdict(dict)


def add(start, end, w):
    nonlocal price
    for x, y in get_way(start, end):

        if x not in price:
            price[x] = defaultdict(lambda: 0)

        if y not in price:
            price[y] = defaultdict(lambda: 0)

        price[x][y] += w
        price[y][x] += w


def get_price(start, end):
    result = 0
    for x, y in get_way(start, end):
        if x in price:
            result += price[x][y]
    return result


@lru_cache(maxsize=1000)
def get_way(start, end):
    def _get_raw_way():
        nonlocal start, end
        l_way, r_way = [start], [end]
        while True:
            l = l_way[-1] // 2
            if l:
                l_way.append(l)
            r = r_way[-1] // 2
            if r:
                r_way.append(r)

            if r_way[-1] == start:
                return r_way
            union = set(l_way) & set(r_way)
            if union:
                # print(l_way)
                # print(r_way)
                r_way = r_way[:r_way.index(max(union))]
                l_way = l_way[:l_way.index(max(union))]
                # print(l_way)
                # print(r_way)
                # print(r_way)
                #del r_way[-1]
                r_way.reverse()
                return l_way + [union.pop()] + r_way

    # print(_get_raw_way())
    a, b = tee(_get_raw_way())
    next(b, None)
    return list(zip(a, b))


#
q = int(input())
for _ in range(q):
    data = list(map(int, input().split(' ')))
    if data[0] == 1:
        add(data[1], data[2], data[3])
    else:
        print(get_price(data[1], data[2]))

#print(get_way(568636620057521218, 935366325112217858))
