for i in range(int(input())):
    n = int(input())
    res = (pow(n - 1, 2) + pow(n, 3))
    print(res % 1000000007)
