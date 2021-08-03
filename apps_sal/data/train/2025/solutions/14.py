from math import sqrt
n = int(input())

a = []
y = ''

if n > 1:
    for i in range(2, n + 1):
        k = 0
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                k = 1
        if k == 0:
            a.append(i)

k = 0
for i in range(len(a)):
    for j in range(1, 10):
        if a[i]**j <= n:
            k = k + 1
            y = y + str(a[i]**j) + ' '


if n == 1:
    print(0)
else:
    print(k)
    print(y)
