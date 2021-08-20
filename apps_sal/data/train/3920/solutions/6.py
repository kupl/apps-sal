def hamming_distance(a, b):
    (A, B) = ([], [])
    a1 = str(bin(a)[2:])
    print(a1)
    [A.append(i) for i in a1]
    b1 = str(bin(b)[2:])
    print(b1)
    [B.append(i) for i in b1]
    distance = 0
    print(A)
    if len(A) < len(B):
        zeros = ['0'] * (len(B) - len(A))
        A = zeros + A
    elif len(A) > len(B):
        zeros = ['0'] * (len(A) - len(B))
        B = zeros + B
    else:
        pass
    print(A)
    for i in range(0, len(A)):
        if A[i] != B[i]:
            distance += 1
    return distance
