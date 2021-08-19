for i in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if a == b:
        print(a * b)
    else:
        print((a + b - 1) * 2)
