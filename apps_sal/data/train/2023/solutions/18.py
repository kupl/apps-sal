import math
n = int(input())
a = math.sqrt(n)
b = math.ceil(a)
a = math.floor(a)
if n - a * a <= a:
    for i in range(a):
        for j in range(a):
            print(a * (i + 1) - j, end=' ')
    if b > a:
        k = n
        while k >= a * a + 1:
            print(k, end=' ')
            k -= 1
else:
    for i in range(a):
        for j in range(b):
            print(b * (i + 1) - j, end=' ')
    if b > a:
        k = n
        while k >= a * b + 1:
            print(k, end=' ')
            k -= 1
