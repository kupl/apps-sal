import sys
import collections
n, q = list(map(int, input().split()))

M = {}

Q = collections.deque()
n = 1
s = 0
m = 0
L = []
for i in range(q):
    c, x = list(map(int, input().split()))

    if c == 1:
        if x not in M:
            M[x] = collections.deque()

        M[x].append(n)
        Q.append(x)

        n += 1
        s += 1

    elif c == 2:
        if x in M:
            s -= len(M[x])

            M[x] = collections.deque()

    else:
        while x > m:
            z = Q.popleft()

            if z in M and len(M[z]) > 0 and M[z][0] <= x:
                s -= 1
                M[z].popleft()

            m += 1
    L.append(s)
sys.stdout.write('\n'.join(map(str, L)))
