n = int(input())
a = tuple(map(int, input().split()))
b = []
s = [0] * n
for i in range(n):
    b.append((a[i], i))
b.sort(reverse=True)
b.append((0, 0))
MIN = 10**9
for i in range(n):
    MIN = min(MIN, b[i][1])
    s[MIN] += (i + 1) * (b[i][0] - b[i + 1][0])
for x in s:
    print(x)
