n = int(input())
while n > 0:
    (a, b) = list(map(int, input().split()))
    if b - a == 0:
        print(0)
    elif b - a > 0:
        if (b - a) % 2:
            print(1)
        elif (b - a) % 2 == 0 and (b - a) % 4:
            print(2)
        else:
            print(3)
    elif (b - a) % 2:
        print(2)
    else:
        print(1)
    n -= 1
