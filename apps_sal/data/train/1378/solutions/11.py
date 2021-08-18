a, n, k = map(int, input().split())
L = [0] * k
for i in range(k):
    L[i] = a % (n + 1)
    a = a // (n + 1)
for j in L:
    print(j, end=' ')
