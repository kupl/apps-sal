def factor(N):
    Z = []
    N = int(N)
    p = int(N**(0.5))
    for i in range(1, p):
        if(N % i == 0):
            Z.append(i)
            Z.append(int(N / i))
    Z.sort()
    return Z


x = int(input())
for y in range(x):
    i, j = list(map(int, input().split()))
    if(((j * (j + 1)) / 2) > i):
        print(-1)
    else:
        p = (j * (j + 1)) / 2
        b = int(i / p)
        A = factor(i)
        s = len(A)
        if b in A:
            print(b)
        else:
            for y in range(1, s):
                if(A[y - 1] <= b < A[y]):
                    print(A[y - 1])
