t = int(input())
while t > 0:
    t -= 1
    a, d, k, n, inc = map(int, input().split())
    s = a
    count = 1
    for i in range(1, n):
        if count == k:
            d += inc
            count = 0
        s = s + d
        count += 1

    print(s)
