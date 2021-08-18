
n = int(input())
a = list(map(int, input().split()))

cnt = {}

for i in range(n):
    if a[i] in cnt:
        cnt[a[i]][0] = min(cnt[a[i]][0], i)
        cnt[a[i]][1] += 1
    else:
        cnt[a[i]] = [i, 1]

mins = [[k, cnt[k][0], cnt[k][1]] for k in cnt]
mins.append([0, 0, 0])
mins.sort(reverse=True)
ans = [0] * n

for i in range(len(mins) - 1):
    k, cntk, l = mins[i][0], mins[i][1], mins[i][2]
    ans[cntk] += (k - mins[i + 1][0]) * l
    mins[i + 1][2] += l
    if mins[i + 1][1] > mins[i][1]:
        mins[i + 1][1] = mins[i][1]

for ai in ans:
    print(ai)
