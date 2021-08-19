a = int(input(''))
A = []
for m in range(a):
    (x, y, z) = [int(q) for q in input('').split()]
    B = [x, y, z]
    A.append(B)
for m in range(a):
    A1 = max(A[m])
    A[m].remove(A1)
    A2 = max(A[m])
    print(A2)
