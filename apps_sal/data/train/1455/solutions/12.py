n = int(input())
g = [int(x) for x in input().split()]
m = int(input())
while m > 0:
    q = [int(x) for x in input().split()]
    k = g[q[0] - 1:q[1]]
    k.sort()
    s = 0
    for i in range(0, len(k) - 1):
        s += (k[i + 1] - k[i]) ** 2
    print(s)
    m -= 1
