from sys import stdin, stdout

input = stdin.readline

t = int(input())
while t:
    t -= 1
    n, m = list(map(int, input().split()))

    a = []
    for i in range(1, 11, 1):
        a.append((m * i) % 10)

    sum = 0
    for i in a:
        sum += i

    x = n // m
    res = (x // 10) * sum
    x %= 10
    for i in range(x):
        res += a[i]

    print(res)

