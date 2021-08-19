def solve():
    n = int(input())
    l = list(map(int, input().split()))
    t_2 = 0
    tn_2 = 0
    for i in range(len(l)):
        if l[i] > 2:
            tn_2 += 1
        elif l[i] == 2:
            t_2 += 1
    ans = tn_2 * (tn_2 - 1) / 2
    ans += t_2 * tn_2
    print(int(ans))


def __starting_point():
    t = int(input())
    while t != 0:
        solve()
        t -= 1


__starting_point()
