import sys
rl = sys.stdin.readline
T = int(rl())
for t in range(T):
    P = int(rl())
    T = (P + 1) // 2
    F = list(map(int, rl().split()))[1:]
    numtorn = int(rl())
    t = sum(range(1, P + 1)) - sum(F)
    K = T - numtorn
    print('%.4f' % (t * K / float(T)))
