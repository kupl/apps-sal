t = int(input())
for i in range(int(t)):
    A, B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    for j in range(A * B):
        if C[j] > D[j]:
            D[j] = 0
        else:
            C[j] = 0
    C.sort(reverse=True)
    D.sort(reverse=True)
    v = 0
    j = 0
    k = 0
    for _ in range(A):
        if C[j] > D[k]:
            v += 1
            j += 1
            k += B - 1
        else:
            k += B
    print(v)
