import sys, collections
def inp():
    return map(int, input().split())
n, q = inp()
Q = collections.deque()
A = n * [0]
B = A[:]
L = []
s = n = 0
for _ in range(q):
    typeq, x = inp()
    if typeq == 1:
        x -= 1
        Q.append(x)
        B[x] += 1
        A[x] += 1
        s += 1
    elif typeq == 2:
        x -= 1
        s -= A[x]
        A[x] = 0
    else:
        while x > n:
            n += 1
            y = Q.popleft()
            B[y] -= 1
            if (B[y] < A[y]):
                A[y] -= 1
                s -= 1
    L.append(s)
sys.stdout.write('\n'.join(map(str,L)))
