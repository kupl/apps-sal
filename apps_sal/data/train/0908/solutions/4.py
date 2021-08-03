MAX = 10**9 + 100
a = []
i = 1
x = 1
while x <= MAX:
    x = (i * (i + 1)) / 2
    a.append(x)
    i += 1
l = len(a)
t = int(input())
while t != 0:
    n = int(input())
    i = 0
    while n >= a[i] and i < l:
        i += 1
    print(i)
    t -= 1
