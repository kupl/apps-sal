import sys
T = int(sys.stdin.readline().strip())

for t in range(T):
    (n, m , a, b) = list(map(int, sys.stdin.readline().strip().split(" ")))
    if n * a != m * b: print("NO"); continue
    res = [["0" for _ in range(m)] for _ in range(n)]
    pt = 0
    for i in range(n):
        for j in range(a):
            res[i][pt] = "1"
            pt = (pt +1)%m
    print("YES")
    for i in range(n):
        print("".join(res[i]))

