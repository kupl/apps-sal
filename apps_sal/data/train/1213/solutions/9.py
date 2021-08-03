# cook your dish here
for _ in range(int(input())):
    x1, x2, x3, v1, v2 = map(int, input().split())

    if (x3 - x1) / v1 > (x2 - x3) / v2:
        print("Kefa")
    elif (x3 - x1) / v1 < (x2 - x3) / v2:
        print("Chef")
    else:
        print("Draw")
