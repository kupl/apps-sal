input()
a = list(input().split())
ans = 0
while len(a) > 0:
    b = a[1:].index(a[0]) + 1
    ans += b - 1
    a = a[1:b] + a[b + 1:]
print(ans)
