def ok(x):
    if x == 0:
        return False
    return x & (x - 1)


n = int(input())
arr = list(map(int, input().split()))
f = [0] * (2000020)
for i in arr:
    f[i] += 1
ans = 0
for i in range(2000010):
    if f[i] % 2 == 1:
        ans += 1
        f[i] -= 1
    f[i + 1] += (f[i] // 2)
print(ans)
