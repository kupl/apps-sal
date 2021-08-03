import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    if m == 1:
        s = p[0]
        b = [0] * n
        b[s] = 0
        for i in range(n):
            if i < s or i > s:
                b[i] = abs(s - i)
        print(*b)
    else:
        t = min(p)
        r = max(p)
        k = []
        r1 = [0] * n
        t1 = [0] * n
        t1[t] = 0
        r1[r] = 0
        for i in range(n):
            if i < t or i > t:
                t1[i] = abs(t - i)
            if i < r or i > r:
                r1[i] = abs(r - i)
        for i in range(n):
            k.append(max(t1[i], r1[i]))
        print(*k)
