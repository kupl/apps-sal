for _ in range(int(input())):
    n = int(input())
    x = 0
    for i in range(n):
        a = int(input())
        if a > x:
            x = a
    print(x)
