for i in range(int(input())):
    x = int(input())
    a = x * x * x + (x - 1) * (x - 1)
    print(a % 1000000007)
