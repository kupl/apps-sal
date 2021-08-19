import sys


def input():
    return sys.stdin.readline().rstrip('\r\n')


def inp():
    return list(map(int, sys.stdin.readline().rstrip('\r\n').split()))


sys.setrecursionlimit(10 ** 5)
a = str(input())
n = len(a)
st = [float('inf') for i in range(4 * len(a))]


def build(a, ind, start, end):
    if start == end:
        st[ind] = [a[start]] if ord(a[start]) % 2 == 0 else []
    else:
        mid = (start + end) // 2
        build(a, 2 * ind + 1, start, mid)
        build(a, 2 * ind + 2, mid + 1, end)
        st[ind] = list(set(st[2 * ind + 1] + st[2 * ind + 2]))


build(a, 0, 0, n - 1)


def query(ind, l, r, start, end):
    if start > r or end < l:
        return []
    if l <= start <= end <= r:
        return st[ind]
    mid = (start + end) // 2
    return list(set(query(2 * ind + 1, l, r, start, mid) + query(2 * ind + 2, l, r, mid + 1, end)))


for i in range(int(input())):
    (l, r) = inp()
    ans = query(0, l - 1, r - 1, 0, n - 1)
    print(len(ans))
