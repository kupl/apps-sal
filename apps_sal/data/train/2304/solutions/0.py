N = int(input())
M = len(input())
O = 10**9 + 7
D = [pow(-~O // 2, M, O)] + [0] * N
for _ in '_' * N:
    D = [D[0] + D[1]] + [(i + 2 * j) % O for i, j in zip(D[2:] + [0], D[:-1])]
print(D[M])
