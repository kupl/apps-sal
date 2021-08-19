t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if sum(l) != n or max(l) == n:
        print('-1')
    else:
        ans = []
        for i in range(n):
            for j in range(l[i]):
                ans.append(i + 1)
        for i in range(len(ans)):
            if ans[i] == i + 1:
                for j in range(len(ans)):
                    if ans[j] != i + 1:
                        (ans[i], ans[j]) = (ans[j], ans[i])
                        break
        print(*ans)
