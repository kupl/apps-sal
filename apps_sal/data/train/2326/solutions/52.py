n = int(input())
a = [[int(i), j] for (j, i) in enumerate(input().split())]
a.sort(reverse=1)
a.append([0, n - 1])
ans = [0] * n
j = n - 1
for i in range(n):
    j = min(j, a[i][1])
    ans[j] += (i + 1) * (a[i][0] - a[i + 1][0])
print('\n'.join(map(str, ans)))
