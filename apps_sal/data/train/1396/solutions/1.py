test = int(input())
for _ in range(test):
    n, m, x, y = map(int, input().split())
    if (n - 1) % x == 0 and (m - 1) % y == 0:
        print("Chefirnemo")
    elif (n - 2) % x == 0 and (m - 2) % y == 0 and (n - 2) >= 0 and (m - 2) >= 0:
        print("Chefirnemo")
    else:
        print("Pofik")
