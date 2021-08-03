
T = int(input())

for t in range(T):
    M = int(input())
    A = []
    for a in range(2 * M + 1):
        if a != M:
            b = (a * M) / (a - M)
            if (a * b) % M == 0 and b > 0:
                A.append(a)
    print(len(A))
    for i in range(len(A)):
        print(A[i])
