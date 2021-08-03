def tidyNumber(n):
    A = []
    Count = 0
    for i in str(n):
        A.append(int(i))
    for i in range(1, len(A)):
        if A[i - 1] > A[i]:
            return False
    return True
