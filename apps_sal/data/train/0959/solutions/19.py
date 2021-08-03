t = int(input())

for _ in range(t):
    n = int(input())

    a = [int(x) for x in input().split()]
    a.sort()

    for i in range(n // 2):
        a[i] = a[i] * (-1)

    print(sum(a))
