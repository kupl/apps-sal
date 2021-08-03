n = int(input())
A = [int(a) for a in input().split(' ')]
R = sorted(A)

for i in range(n):
    if A[i] == R[-1]:
        A[i] = R[0]
    else:
        A[i] = R[R.index(A[i]) + 1]

print(' '.join([str(a) for a in A]))
