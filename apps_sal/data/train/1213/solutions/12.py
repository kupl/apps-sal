for i in range(int(input())):
    x1, x2, x3, v1, v2 = list(map(int, input().split()))

    timechef = abs(x3 - x1) / v1
    timekefa = abs(x2 - x3) / v2
    if timechef > timekefa:
        print("Kefa")
    elif timekefa > timechef:
        print("Chef")
    else:
        print("Draw")
