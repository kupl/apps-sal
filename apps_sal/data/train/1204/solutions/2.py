import sys
import math
# from collections import defaultdict, deque


def fout(s, end='\n'): sys.stdout.write(str(s) + end)
def fin(): return sys.stdin.readline().strip()


t = int(fin())
while t > 0:
    t -= 1
    s = fin()
    r = fin()
    un = isl = 0  # unequal
    count = 0
    eqisl = []
    count2 = 0
    for i in range(len(r)):
        if s[i] == r[i]:
            if un == 0:
                continue
            count2 += 1
            if count > 0:
                isl += 1
                count = 0
        else:
            if count2 > 0:
                eqisl.append(count2)
                count2 = 0
            un += 1
            count += 1
    if count > 0:
        isl += 1
    eqisl.sort()
    ans = un * isl
    for i in range(len(eqisl)):
        un += eqisl[i]
        isl -= 1
        ans = min(ans, un * (isl))
    print(ans)
