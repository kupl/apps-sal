n = int(input())
a = []
s = []

for i in range(n):
    x = int(input())
    a.append(x * n + i)
    s.append(1)

a.sort()
a.reverse()
a.append(-1)
Sum = 0

Have = True

result = []

for i in range(n - 1):
    l = 0
    r = n

    val = (a[i] // n) + s[i] + s[i] - n

    while (l < r):
        m = (l + r + 2) // 2

        if (a[m] >= val * n):
            l = m
        else:
            r = m - 1

    if((a[l] // n) != val):
        Have = False
        break

    s[l] += s[i]
    Sum  += s[i]
    result.append([a[i] % n,a[l] % n])

if (Sum != (a[n - 1] // n)):
    Have = False

if (Have == False):
    print("-1")
else:
    for e in result:
        print(e[0] + 1,end = " ")
        print(e[1] + 1)

