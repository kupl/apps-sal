(N, *L) = map(int, open(0).read().split())
A = [0] * N
B = [0] * N
n = 10 ** 10
flag = False
for (i, (a, b)) in enumerate(zip(*[iter(L)] * 2)):
    A[i] = a
    B[i] = b
    if a != b:
        flag = True
    if a > b:
        n = min(n, b)
print(sum(A) - n if flag else 0)
