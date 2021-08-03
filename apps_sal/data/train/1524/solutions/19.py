import sys
t = int(eval(input("")))
while t:
    m, n = list(map(int, sys.stdin.readline().split()))
    prod = n
    prod *= (n - 1)**(m - 1)
    print(prod % 1000000007)
    t -= 1
