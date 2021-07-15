def jumbled_string(s, n):
    combine = lambda s : s[0::2] + s[1::2]
    for _ in range(n%multiplicativeOrder(2, len(s))):
        s = combine(s)
    return s

def GCD (a, b ) : 
    if (b == 0 ) : 
        return a 
    return GCD( b, a % b ) 

def multiplicativeOrder(A, N) : 
    if (GCD(A, N ) != 1) : 
        return multiplicativeOrder(A, N-1)
    result = 1

    K = 1
    while (K < N) : 
        result = (result * A) % N 
        if (result == 1) : 
            return K 
        K = K + 1
    return -1


