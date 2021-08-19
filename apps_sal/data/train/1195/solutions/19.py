for _ in range(int(input())):
    (n, a, b, c, d, p, q, y) = map(int, input().split())
    ar = [int(x) for x in input().split()]
    temp1 = abs(ar[a - 1] - ar[c - 1]) * p
    if temp1 > y:
        temp1 = 10 ** 9
    elif temp1 == y:
        temp1 += abs(ar[c - 1] - ar[d - 1]) * q + abs(ar[d - 1] - ar[b - 1]) * p
    elif temp1 < y:
        temp1 += abs(ar[c - 1] - ar[d - 1]) * q + abs(ar[d - 1] - ar[b - 1]) * p + abs(temp1 - y)
    temp2 = abs(ar[a - 1] - ar[b - 1]) * p
    print(min(temp1, temp2))
