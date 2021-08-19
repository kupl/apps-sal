import sys
import numpy
f = sys.stdin

#f = open('HILLJUMP.txt')
# N and Q, the number of hills and number of operations.
n, q = [int(x) for x in f.readline().split()]
# A1, A2, ..., AN denoting the initial heights of the hills.
a = [int(x) for x in f.readline().split()]
# Each of the next Q lines describes an operation.
t2 = []
for _ in range(0, q):
    op = [int(x) for x in f.readline().split()]
    if op[0] == 1:
        # Type 1, and it will be followed by two integers i and k.
        p = op[1] - 1
        jumps = 0
        for i in range(p + 1, n):
            dist = i - p
            if dist > 100:
                break
            else:
                # jump, if dist <= 100
                vp = a[p]
                vi = a[i]
                for arr2 in t2:
                    l = arr2[1] - 1
                    r = arr2[2] - 1
                    if p >= l and p <= r:
                        vp += arr2[3]
                    if i >= l and i <= r:
                        vi += arr2[3]
                if vp < vi:
                    p = i
                    jumps += 1
            if jumps >= op[2]:
                break
        print(p + 1)
    else:
        # three integers L, R and X.
        #a = a[:op[1]-1] + map(lambda x: x+op[3], a[op[1]-1:op[2]]) + a[op[2]:]
        #a[op[1]-1:op[2]] = map(lambda x: x+op[3], a[op[1]-1:op[2]])
        t2.append(op)
# f.close()
