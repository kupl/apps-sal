n, d = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

k = 0
S = 0

for i in range(2, n):
    while x[i] - x[k] > d:
        k = k + 1
    P = i - k
    S += P * (P - 1) // 2

print(S)
