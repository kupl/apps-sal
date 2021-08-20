n = input()
a = [0] * 1000021
ans = 0
b = 0
for u in map(int, input().split()):
    a[u] += 1
for u in a:
    b += u
    if b & 1:
        ans += 1
    b >>= 1
print(ans)
