def pf(a):
    M = max(a)
    for j in range(len(a)):
        a[j] = M - a[j]


(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
if k > 0:
    pf(a)
    if k % 2 == 0:
        pf(a)
print(' '.join(map(str, a)))
