n, k, p = list(map(int, input().split()))
a = list(map(int, input().split()))
newar = []
for i in range(n):
    newar.append((a[i], i))
newar.sort(key=lambda x: x[0])
revmap = [0] * n
ans = [0] * n
ctr = 1

ans[0] = ctr
for i in range(n):
    revmap[newar[i][1]] = i

    if i != n - 1:
        if(newar[i + 1][0] - newar[i][0]) <= k:
            ans[i + 1] = ctr
        else:
            ctr += 1
            ans[i + 1] = ctr
for _ in range(p):
    A, B = list(map(int, input().split()))
    if ans[revmap[A - 1]] == ans[revmap[B - 1]]:
        print('Yes')
    else:
        print('No')
