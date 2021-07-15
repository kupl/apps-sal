import collections
t = int(input())
for i in range(t):
    s = list(input())
    c = collections.Counter(s)
    L, R, U, D = c['L'], c['R'], c['U'], c['D']
    if (L == 0 or R == 0) and (U == 0 or D == 0):
        print(0)
    elif L == 0 or R == 0:
        print(2)
        print('UD')
    elif U == 0 or D == 0:
        print(2)
        print('LR')
    else:
        p, q = min(L, R), min(U, D)
        print(2 * p + 2 * q)
        print(p * 'L' + q * 'U' + p * 'R' + q * 'D')
