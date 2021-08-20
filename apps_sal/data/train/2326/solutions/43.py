n = int(input())
a = list(map(int, input().split()))
a = list(zip(a, range(len(a))))
a = sorted(a, reverse=True) + [(0, 0)]
ans = [0] * n
min_ind = 10 ** 9
for i in range(n):
    tmp = a[i][0] - a[i + 1][0]
    min_ind = min(min_ind, a[i][1])
    ans[min_ind] += (i + 1) * tmp
for i in ans:
    print(i)
