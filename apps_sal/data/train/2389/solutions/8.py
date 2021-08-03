import sys
def input(): return sys.stdin.readline().strip()


nxt = {'R': 'G', 'G': 'B', 'B': 'R'}

T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    s = input()
    res = []
    for start in ['R', 'G', 'B']:
        mis = []
        cur = start
        for j in range(k):
            if s[j] != cur:
                mis.append(1)
            else:
                mis.append(0)
            cur = nxt[cur]
        res.append(sum(mis))
        for j in range(k, n):
            res.append(res[-1] + int(s[j] != cur) - mis[j - k])
            if s[j] != cur:
                mis.append(1)
            else:
                mis.append(0)
            cur = nxt[cur]
    print(min(res))
