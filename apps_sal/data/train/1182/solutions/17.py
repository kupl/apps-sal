T = int(input())
for t in range(T):
    M = int(input())
    A = []
    for a in range(M + 1, 2 * M + 1):
        if float(a * a / (a - M)).is_integer() == True and a * M / (a - M) > 0:
            A.append(a)
    print(len(A))
    for i in range(len(A)):
        print(A[i])
