# cook your dish here
from sys import stdin, stdout
def I1(): return int(stdin.readline())


T = 0
for _ in range(I1()):
    m = I1()
    li2 = [12, 3, 6, 9]
    d = {'A': [0, 0, 0, 0], 'B': [0, 0, 0, 0], 'C': [0, 0, 0, 0], 'D': [0, 0, 0, 0]}
    for i in range(m):
        x, t = list(map(str, stdin.readline().split()))
        t = int(t)
        d[x][li2.index(t)] += 1
    # print(d)
    n = 4
    ans = []
    cost = [100, 75, 50, 25]
    for i in range(n):
        li1 = []
        li1.append(d['A'][i])
        for j in range(n):
            if j != i:
                li1.append(d['B'][j])
                for k in range(n):
                    if k != i and k != j:
                        li1.append(d['C'][k])
                        for l in range(n):
                            if l != i and l != j and l != k:
                                li1.append(d['D'][l])
                                c = 0
                                z = 0
                                for s in sorted(li1, reverse=True):
                                    if s == 0:
                                        c -= 100
                                    else:
                                        c += s * cost[z]
                                    z += 1
                                if c != 0:
                                    ans.append(c)
                                li1.pop()
                        li1.pop()
                li1.pop()
        li1.pop()
    # print(ans)
    a = max(ans)
    print(a)
    T += a
print(T)
