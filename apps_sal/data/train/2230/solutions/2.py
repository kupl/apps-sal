import sys

def solve():
    n = int(sys.stdin.readline())
    p = [int(pi) for pi in sys.stdin.readline().split()]
    a = [int(ai) - 1 for ai in sys.stdin.readline().split()]
    b = [int(bi) - 1 for bi in sys.stdin.readline().split()]
    m = int(sys.stdin.readline())
    c = [int(ci) - 1 for ci in sys.stdin.readline().split()]

    p_col = [[] for i in range(3)]

    for i in range(n):
        p_col[a[i]].append(p[i])

        if a[i] != b[i]:
            p_col[b[i]].append(p[i])

    for i in range(3):
        p_col[i].sort()

    used = set()

    l = [0]*3
    ans = [-1]*m

    for k, cj in enumerate(c):
        for i in range(l[cj], len(p_col[cj])):
            if p_col[cj][i] not in used:
                ans[k] = p_col[cj][i]
                used.add(p_col[cj][i])
                l[cj] = i + 1
                break

    print(*ans)

def __starting_point():
    solve()
__starting_point()
