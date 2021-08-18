import math


def read(): return list(map(int, input().strip().split()))
def read_arr(x): return [read() for _ in range(x)]


ans = []

t = int(input().strip())


def mincost(n, m, arr, s, p, q):
    cost = 0
    for t in range(n + m - 1):
        cc = s[t]
        curr = 0
        ct = 0
        start = max(0, t - (m - 1))
        end = min(n, t + 1)
        for i in range(start, end):
            j = t - i
            if j >= m:
                break
            curr += (cc ^ (arr[i][j]))
            ct += 1
        cost1 = q + ((ct - curr) * p)
        cost2 = (curr * p)
        cost += min(cost1, cost2)
    return cost


for i in range(t):
    cn, cm = read()
    carr = read_arr(cn)
    cs = [int(x) for x in input().strip()]
    cp, cq = read()
    ans.append(mincost(cn, cm, carr, cs, cp, cq))
print("\n".join([str(x) for x in ans]))
