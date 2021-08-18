from copy import copy
T = int(input())


def dfs(lst):
    topi = -1
    topv = 0
    for i, e in enumerate(lst):
        if topv < e:
            topv = e
            topi = i
    if topi == 0 or topi == len(lst) - 1:
        return 1

    else:
        return 1 + min(dfs(lst[:topi]),
                       dfs(lst[topi + 1:]))


for t in range(T):
    N = int(input())
    H = list(map(int, input().split()))
    ans = dfs(H)

    print(ans)
