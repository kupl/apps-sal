import sys
from collections import defaultdict
from itertools import permutations, combinations
import string
from heapq import heapify, heappush, heappop


def solve():
    sys.setrecursionlimit(int(1e5))
    MOD = int(1e9) + 7
    alphabets = string.ascii_lowercase; digits = string.digits
    glo = globals; loc = locals;
    get_arr = lambda type_=int: list(map(type_, sys.stdin.readline().rstrip('\n').split()))
    inp = lambda type_=int: type_(sys.stdin.readline().rstrip('\n'))
    pair = lambda type_=int: list(map(type_, sys.stdin.readline().rstrip('\n').split(' ')))
    debug = lambda *args: [(args[i], eval(args[i], args[-1])) for i in range(len(args)-1)]
    filter_ = lambda fn, arr: list(filter(fn, arr))
    map_ = lambda fn, arr: list(map(fn, arr))
    t = inp()
    for _ in range(t):
        n = inp()
        grid = []
        for i in range(n):
            grid.append(inp(str))
        d = defaultdict(int)
        res = n
        l = []
        for i in range(n):
            s = grid[i]
            for j in range(n):
                if s[j] == '1':
                    d[i] = j
                    l.append(j)
                    break
        #print(d)
        # print(l)
        for i in range(len(grid)):
            my_set = set()
            my_set2 = set()
            for j in range(i, len(grid)):
                my_set.add(l[j])
                my_set2.add(d[l[j]])
                if my_set == my_set2 and len(my_set) > 1:
                    res += 1
        print(res)


solve()

