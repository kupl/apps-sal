N, T = map(int, input().split())
A = list(map(int, input().split()))
x = 10**9
d = 0
ans = 0
for a in A:
    if a < x:
        x = a
    elif a - x > d:
        d = a - x
        ans = 1
    elif a - x == d:
        ans += 1
print(ans)
