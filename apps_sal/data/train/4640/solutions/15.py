def int_diff(A, n):
    return sum(abs(A[j]-A[i])==n for i in range(len(A))for j in range(i+1,len(A)))

