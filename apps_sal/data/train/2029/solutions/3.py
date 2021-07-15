N = int(input())

if N % 2 == 0:
    print("NO")
else:
    print("YES")
    X = [-1] * (2*N)
    a = 1
    b = 2 * N
    i = 0
    while i < N:
        X[i] = a
        X[i+N] = a + 1
        i += 1
        if i >= N: break
        X[i] = b
        X[i+N] = b - 1
        i += 1
        a += 2
        b -= 2
    
    print(*X)

