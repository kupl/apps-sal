try:
    for _ in range(int(input())):
        n = int(input())
        r = n ** 3 + (n - 1) ** 2
        print(r % 1000000007)
except:
    pass
