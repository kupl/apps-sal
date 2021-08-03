t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().strip().split(" "))
    n -= 1
    m -= 1
    rx = n % x
    ry = m % y
    if (rx == 0 and ry == 0) or (rx == 1 and ry == 1):
        print("Chefirnemo")
    elif (x == 1 and ry == 1 and n > 0) or (m > 0 and y == 1 and rx == 1):
        print("Chefirnemo")
    else:
        print("Pofik")
