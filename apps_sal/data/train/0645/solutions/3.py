def solve():
    n = int(input())
    k = int(input())
    cnt1 = k % n
    cnt0 = n - cnt1
    if(cnt1 < cnt0):
        print(2 * cnt1)
    elif(cnt1 > cnt0):
        print(2 * cnt0)
    else:
        print(2 * cnt1 - 1)


def __starting_point():
    t = int(input())
    for _1 in range(t):
        solve()


__starting_point()
