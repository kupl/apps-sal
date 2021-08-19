for t in range(int(input())):
    n = int(input())
    li = [0] + list(map(int, input().split()))
    ans = [0, li[1]]
    for i in range(2, n + 1):
        ans += [max(ans[i - 1] + li[i] * i, ans[i - 2] + li[i - 1] * i + li[i] * (i - 1))]
    print(ans[-1])
