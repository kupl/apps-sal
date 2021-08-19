t = int(input())
for i in range(t):
    n = int(input())
    a = [0] * 8
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        if x <= 8:
            if a[x - 1] < y:
                a[x - 1] = y
    sum = 0
    for j in a:
        sum += j
    print(sum)
