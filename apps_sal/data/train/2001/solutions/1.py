x, d = list(map(int, input().split()))
arr = []
n = 0
s = ''
while x > 0:
    s += str(x % 2)
    x //= 2
f = 1
l = 999999999999999999
for i in range(len(s)):
    if int(s[i]):
        arr += [f] * i + [l]
        f += d
        l -= d
        n += i + 1
if n == -1:
    print(-1)
else:
    print(n)
    print(*arr)





