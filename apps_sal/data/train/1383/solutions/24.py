import math
cn = [0, 0]
for _ in range(10000):
    cn.append(1)
for i in range(2, 10000):
    if(cn[i] == 1):
        j = 2 * i
        while(j < 10000):
            cn[j] = 0
            j += i
for i in range(1, 10000):
    cn[i] += cn[i - 1]
t = int(input())
for _ in range(t):
    n, k1, k2 = (int(i) for i in input().split())
    p1, p2, p3, p4 = (int(i) for i in input().split())
    s1 = math.floor(math.sqrt(k1 - 1))
    s2 = math.floor(math.sqrt(k2))
    pr = cn[s2] - cn[s1]
    ans = p1 * pr + p2 * (s2 - s1 - pr) + p3 * (k2 - k1 + 1 - s2 + s1)
    print(ans % 100000007)
