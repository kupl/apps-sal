from sys import stdin


def solve():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    x = int(stdin.readline())
    a.sort()
    ans = 0
    if x == 0:
        ans = 0
    elif x < n:
        op1 = max(0, -a[x - 1])
        ans += op1 * x
        for i in range(x - 1):
            ans += max(0, -(a[i] + op1))
    else:
        for i in range(n):
            if a[i] < 0:
                ans += -a[i]
    print(ans)


def __starting_point():
    solve()


__starting_point()
