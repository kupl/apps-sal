t = int(input())
for i in range(0, t):
    x1, x2, x3, V1, V2 = list(map(int, input().split()))
    if (x3 - x1) / V1 < (x2 - x3) / V2:
        print("Chef")
    elif (x3 - x1) / V1 > (x2 - x3) / V2:
        print("Kefa")
    else:
        print("Draw")
