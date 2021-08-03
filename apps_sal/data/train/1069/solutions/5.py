a = int(input(""))
A = []
for m in range(a):
    x, y = [int(x) for x in input("").split()]
    B = [x, y]
    A.append(B)
for m in range(a):
    print(A[m][0] + A[m][1])
