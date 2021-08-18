for _ in range(int(input())):
    n = int(input())
    a = [int(X) for X in input().split()]
    x = 0
    for i in a:
        x ^= i
    print(x)
