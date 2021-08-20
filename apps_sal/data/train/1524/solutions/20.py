import sys
t = int(eval(input('')))
while t:
    (m, n) = list(map(int, sys.stdin.readline().split()))
    prod = n
    for i in range(m - 1):
        prod *= n - 1
    print(prod % 1000000007)
    t -= 1
