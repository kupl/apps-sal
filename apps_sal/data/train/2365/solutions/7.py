import sys
import collections
import threading
import copy


def check(itr, sets):
    d = {}

    def dmap(x):
        return d[x]
    for i in range(len(itr)):
        d[itr[i]] = i
    for perm in sets:
        tmp = sorted(list(map(dmap, perm)))
        if len(tmp) != tmp[-1] - tmp[0] + 1:
            return False

    return True


def main():
    n = int(input())
    sets = []
    start = set()
    for _ in range(n - 1):
        l, *tmp = list(map(int, input().split()))
        sets.append(set(tmp))
        if l == 2:
            start.add(tmp[0])
            start.add(tmp[1])

    ans = collections.deque()
    for i in start:
        permuts = copy.deepcopy(sets)
        next = i
        while len(ans) > 0:
            ans.pop()

        ans.append(next)
        while len(ans) < n:
            q = []
            for permut in permuts:
                if next in permut:
                    permut.remove(next)
                    if len(permut) == 1:
                        q.append(permut)
            if len(q) != 1:
                break
            next = list(q[0])[0]
            ans.append(next)
        if len(ans) == n and check(ans, sets):
            print(*ans)
            return
    print("error")
    return


input = sys.stdin.readline
tnum = int(input())
for _ in range(tnum):
    main()
