import math

t = int(input())

for q in range(t):
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    ma = min(A)
    mb = min(B)
    s = 0
    for i in range(n):
        s += max(A[i] - ma, B[i] - mb)
    print(s)
