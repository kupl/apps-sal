for i in range(int(input())):
    n = int(input())
    x = (n - 1) ** 2 + n ** 3
    if x > 1000000000:
        x = x % 1000000007
    print(x)
