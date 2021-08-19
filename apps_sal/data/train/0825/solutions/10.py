import sys
T = int(sys.stdin.readline().strip())
while T > 0:
    n = int(sys.stdin.readline().strip())
    m = 2 ** (n - 2) + 1
    print(m)
    T = T - 1
