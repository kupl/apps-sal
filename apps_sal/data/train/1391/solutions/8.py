import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip("\r\n")


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    dic = defaultdict(lambda: [])
    for i in range(n):
        a, d, c = list(map(int, input().split()))
        dic[c].append((a, d))
    out = 0
    for i in dic:
        dic[i].sort(key=lambda x: x[1])
        t = 0
        j = 0
        l = len(dic[i])
        while j < l:
            if t <= dic[i][j][0]:
                out += 1
                t = dic[i][j][1]
            j += 1
    print(out)
