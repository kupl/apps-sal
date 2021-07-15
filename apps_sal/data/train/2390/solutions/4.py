SS = []
a = int(input())
for i in range(a):
    x = int(input())
    A = list(map(int, input().split()))
    D = {}
    for j in range(x):
        if A[j] in D:
            D[A[j]] += 1
        else:
            D[A[j]] = 1
    B = []
    for key in D:
        B.append(D[key])
    B.sort(reverse=True)
    w = B[0]
    for j in range(1, len(B)):
        if B[j] < B[j - 1] - 1:
            w += max(0, B[j])
        else:
            B[j] = B[j - 1] - 1
            w += max(0, B[j - 1] - 1)
    SS.append(w)
for s in SS:
    print(s)
