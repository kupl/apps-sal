a = []
a.append(1)
for i in range(1, 100001):
    a.append((a[-1] * i) % 1589540031)
t = int(input())
for i in range(t):
    n = int(input())
    print(a[n])
