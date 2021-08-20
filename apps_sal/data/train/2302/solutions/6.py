import sys
readline = sys.stdin.readline
(N, D) = list(map(int, readline().split()))
A = list(map(int, readline().split())) + [0]
reach = [None] * (N + 2)
reach[-1] = D
for i in range(N + 1):
    r = reach[i - 1]
    a = A[i]
    reach[i] = min(r, abs(r - a))
putter = [0] * (N + 2)
for i in range(N, -1, -1):
    p = putter[i + 1]
    a = A[i]
    if 2 * p + 1 >= a:
        p += a
    putter[i] = p
res = ['NO'] * N
for i in range(N):
    if reach[i - 1] > putter[i + 1]:
        res[i] = 'YES'
Q = int(readline())
print('\n'.join((res[int(i) - 1] for i in readline().split())))
