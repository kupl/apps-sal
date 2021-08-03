import sys


def eprint(*args):
    print(*args, file=sys.stderr)


zz = 1

sys.setrecursionlimit(10**6)
if zz:
    input = sys.stdin.readline
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('all.txt', 'w')
di = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def string(s):
    return "".join(s)


def fori(n):
    return [fi() for i in range(n)]


def inc(d, c, x=1):
    d[c] = d[c] + x if c in d else x


def bo(i):
    return ord(i) - ord('A')


def li():
    return [int(xx) for xx in input().split()]


def fli():
    return [float(x) for x in input().split()]


def comp(a, b):
    if(a > b):
        return 2
    return 2 if a == b else 0


def gi():
    return [xx for xx in input().split()]


def cil(n, m):
    return n // m + int(n % m > 0)


def fi():
    return int(input())


def pro(a):
    return reduce(lambda a, b: a * b, a)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def si():
    return list(input().rstrip())


def mi():
    return map(int, input().split())


def gh():
    sys.stdout.flush()


def isvalid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def bo(i):
    return ord(i) - ord('a')


def graph(n, m):
    for i in range(m):
        x, y = mi()
        a[x].append(y)
        a[y].append(x)


t = fi()

while t > 0:
    t -= 1
    n = fi()
    p = li()
    a = [[] for i in range(n + 1)]
    for i in range(n - 1):
        a[i + 2].append(p[i])
        a[p[i]].append(i + 2)
    subtree = [1] * (n + 1)

    def dfs(i, par=-1):
        for j in a[i]:
            if j != par:
                dfs(j, i)
                subtree[i] += subtree[j]
    dfs(1, -1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            ans[i] = n
        else:
            ans[i] += subtree[i] + ans[p[i - 2]]
    print(max(ans))
