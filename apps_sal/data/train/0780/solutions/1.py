t = int(input())
for i in range(0, t):
    n, m = list(map(int, input().split()))
    p = n % m
    if p % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
