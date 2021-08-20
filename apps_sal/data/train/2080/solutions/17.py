m = int(input())
q = [int(i) for i in input().split()]
q.sort()
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
ans = 0
i = n - 1
while i >= 0:
    d = 0
    while i >= 0 and d < q[0]:
        ans += a[i]
        i -= 1
        d += 1
    d = 0
    while i >= 0 and d < 2:
        d += 1
        i -= 1
print(ans)
