import sys
import collections
(n, q) = list(map(int, input().split()))
M = collections.defaultdict(collections.deque)
Q = collections.deque()
n = 0
s = 0
m = 0
L = []
for i in range(q):
    (c, x) = list(map(int, input().split()))
    if c == 1:
        M[x].append(n)
        Q.append(x)
        n += 1
        s += 1
    elif c == 2:
        y = M.get(x)
        if y:
            s -= len(y)
            del M[x]
    else:
        while x > m:
            z = Q.popleft()
            y = M.get(z)
            if y and y[0] < x:
                s -= 1
                y.popleft()
                if not y:
                    del M[z]
            m += 1
    L.append(s)
sys.stdout.write('\n'.join(map(str, L)))
