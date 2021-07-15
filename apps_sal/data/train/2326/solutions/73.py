from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))

li = [[0, -1]]
for i, e in enumerate(a):
    if e > li[-1][0]:
        li.append([e, i])

li = li[::-1]

a.sort()
acc = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    acc[i] = acc[i+1] + a[i]

ans = [0] * n
sub = 0
ans_prev = 0
for (ep, ip), (e, i) in zip(li, li[1:]):
    j = bisect_right(a, e)
    ans[ip] = acc[j] - e * (n - j)

i_prev = 0
for i in range(1, n):
    if ans[i]:
        ans[i_prev] -= ans[i]
        i_prev = i

print(*ans, sep="\n")

