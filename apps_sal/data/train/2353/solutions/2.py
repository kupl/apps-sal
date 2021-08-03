def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a) + [min(a)]
    for i in range(n):
        a[i] = str(b[b.index(a[i]) + 1])
    print(' '.join(a))
    return


solve()
