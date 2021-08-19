T = int(input())
for t in range(T):
    M = int(input())
    A = []
    for a in range(M + 1, 2 * M + 1):
        b = a * M / (a - M)
        if float(a + b).is_integer() == True and a <= b:
            A.append(a)
    print(len(A))
    for i in range(len(A)):
        print(A[i])
