def go():
    for t in range(int(input())):
        n = int(input())
        v = pow(3, n, 1000000007) + (-3 if n & 1 else 3)
        print(v % 1000000007)


go()
