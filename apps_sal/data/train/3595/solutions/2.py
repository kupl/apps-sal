def work_on_strings(a,b):
    A = list(a); B =list(b)
    #Forward Sort
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i].upper() == B[j] or A[i].lower() == B[j]:
                B[j] = B[j].swapcase()
    #Backwards Sort
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i].upper() == A[j] or B[i].lower() == A[j]:
                A[j] = A[j].swapcase()
    return "".join(str(i) for i in A+B)
