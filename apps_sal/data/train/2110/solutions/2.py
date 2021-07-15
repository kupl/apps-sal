from sys import stdin
stdin.readline()
a = [0] * 1000021
ans = b = 0
for u in map(int, stdin.readline().split()):
    a[u] += 1
for u in a:
    b += u
    ans += b&1
    b >>= 1
print(ans)
