
t = int(input())
A = []
B = []
for i in range(0, t, 1):
    n, k = input().split()
    n = int(n)
    k = int(k)
    if k != 0:
        A.append(n // k)
        B.append(n % k)
    else:
        A.append(0)
        B.append(n)
for i in range(0, t, 1):
    print(A[i], B[i])
