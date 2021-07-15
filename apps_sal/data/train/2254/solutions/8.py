import collections
n, q = list(map(int ,input().split()))
Q = collections.deque()
A = [0] * n
B = A[:]
L = []
s = n = 0
for k in range(q):
    type1, x = list(map(int, input().split()))
    if type1 == 1:
        x -= 1
        Q.append(x)
        B[x] += 1
        A[x] += 1
        s += 1
    if type1 == 2:
        x -= 1
        s -= A[x]
        A[x] = 0
    if type1 == 3:
        while x > n:
            n += 1
            y = Q.popleft()
            B[y] -= 1
            if B[y] < A[y]:
                A[y] -= 1
                s -= 1
    L.append(str(s))
print('\n'.join(L))

