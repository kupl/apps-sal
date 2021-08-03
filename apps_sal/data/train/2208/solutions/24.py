"""
NTC here
"""
from collections import defaultdict
import threading
from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

threading.stack_size(2 ** 27)


def iin(): return int(stdin.readline())


def lin(): return list(map(int, stdin.readline().split()))

# range = xrange
# input = raw_input


class Disjoint_set:

    def __init__(sf, n):
        sf.parent = {i: i for i in range(1, n + 1)}

    def union(sf, x, y):
        sf.link(sf.find_set(x), sf.find_set(y))

    def link(sf, val1, val2):
        sf.parent[val1] = val2

    def find_set(sf, val):
        if sf.parent[val] != val:
            sf.parent[val] = sf.find_set(sf.parent[val])
            return sf.parent[val]
        else:
            return val


def main():
    n, k = lin()

    a = [lin() for i in range(k)]
    da = Disjoint_set(n)
    for i, j in a:
        da.union(i, j)
    ch = defaultdict(int)
    for i in range(1, n + 1):
        # print("CNN",i,da.find_set(da.data[i]).value)
        ch[da.find_set(i)] += 1
    ans = 0
    for i in ch:
        if ch[i]:
            ans += ch[i] - 1
    print(k - ans)


try:
    def __starting_point():
        threading.Thread(target=main).start()
except Exception as e:
    print(e)

__starting_point()
