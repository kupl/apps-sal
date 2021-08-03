import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
imos = []
for i in range(n):
    s, t, x = list(map(int, input().split()))
    imos.append((s - x, x))
    imos.append((t - x, -x))
ans = set()
j = 0
for i in range(q):
    d = int(input())
    imos.append((d, 1e100))
imos.sort()
m = 1e100
flag = False
for t, stop in imos:
    if stop == 1e100:
        if ans:
            if not flag:
                m = min(ans)
                flag = True
            print(m)
        else:
            print((-1))
    elif stop > 0:
        ans.add(stop)
        if stop < m:
            m = stop
            flag = True
    else:
        ans.remove(-stop)
        if m == -stop:
            flag = False
