n = int(input())
a = list(map(int, input().split(' ')))
x = int(input())
a.sort()
ans = 0
if x == 0:
    ans = 0
elif x < n:
    op1 = max(0, -a[x - 1])
    ans += op1 * x
    for i in range(x - 1):
        ans += max(0, -(a[i] + op1))
else:
    for i in range(n):
        if a[i] < 0:
            ans += -a[i]
print(ans)
