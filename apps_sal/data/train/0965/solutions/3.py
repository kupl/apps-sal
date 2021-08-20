for i in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if b == 0:
        print(0, a)
    else:
        print(a // b, a % b)
