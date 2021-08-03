for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    if a == 0:
        print(0, 0)
    elif b == 0:
        print(0, a)
    else:
        print(a // b, a % b)
