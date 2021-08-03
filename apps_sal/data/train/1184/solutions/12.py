import sys
import itertools


def read_line():
    return sys.stdin.readline().split()


s = 0
T = int(read_line()[0])
for i in range(T):
    n = int(read_line()[0])

    cnt = {}
    for j in range(n):
        a, b = read_line()
        if cnt.get((a, b)) == None:
            cnt[(a, b)] = 1
        else:
            cnt[(a, b)] += 1

    best = -(10 ** 18)
    for p in list(itertools.permutations(['A', 'B', 'C', 'D'])):
        cand = 0
        li = []
        for t, f in zip(['12', '3', '6', '9'], p):
            li.append(cnt.get((f, t), 0))
            if li[-1] == 0:
                cand -= 100

        li = sorted(li)

        pr = 25
        for x in li:
            cand += pr * x
            pr += 25

        best = max(best, cand)

    print(best)
    s += best
print(s)
