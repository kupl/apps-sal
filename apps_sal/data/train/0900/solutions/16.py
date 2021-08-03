for i in range(int(input())):
    n = int(input())
    m = 10**9 + 7
    print(10 * (2**(n - 1)) % m)
