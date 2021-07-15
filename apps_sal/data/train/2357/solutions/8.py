P = 10 ** 9 + 7
N, M = map(int, input().split())
A = [int(a) for a in input().split()]
s = sum(A)
u = 1
v = 1
for i in range(M - s + 1, N + M + 1):
    u = u * i % P
for i in range(1, s + N + 1):
    v = i * v % P
print(u * pow(v, P - 2, P) % P)
