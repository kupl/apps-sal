from math import sqrt
def take(): return input().strip()


def cal(): return list(map(int, take().split()))


T = int(take())
for _ in range(T):
    N = take()
    alpha = {}
    s = list(cal())
    for i in s:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1
    for e in sorted(alpha.keys()):
        print(str(e) + ': ' + str(alpha[e]))
