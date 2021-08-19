(n, t) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = float('inf')
c = 0
ans = 0
for i in range(n):
    if a[i] < b:
        b = a[i]
    if a[i] - b == c:
        ans += 1
    elif a[i] - b > c:
        c = a[i] - b
        ans = 1
print(ans)
