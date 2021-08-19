pr = [1] * (10 ** 6 + 1)
pr[0] = pr[1] = 0
for i in range(2, 10 ** 6 + 1):
    if pr[i]:
        for j in range(i * i, 10 ** 6 + 1, i):
            pr[j] = 0
ans = [0]
for i in range(1, 10 ** 6 + 1):
    if pr[i]:
        ans.append(ans[-1] + i)
    else:
        ans.append(ans[-1])
t = int(input())
for _ in range(t):
    n = int(input())
    print(ans[n])
