import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    max_ = 0
    ans = []
    for val in p:
        if max_ < val:
            if cnt == 0:
                pass
            else:
                ans.append(cnt)
            max_ = val
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    len_ans = len(ans)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(len_ans):
        val = ans[i]
        for j in range(n)[::-1]:
            if j + 1 - val < 0:
                break
            dp[j + 1] |= dp[j + 1 - val]
    if dp[-1]:
        print('YES')
    else:
        print('NO')
