P = 10 ** 9 + 7
N, M = map(int, input().split())
A = [int(a) for a in input().split()]
u = 1
v = 1
for i in range(sum(A) + N):
    u = u * (N + M - i) % P
    v = (i + 1) * v % P
print(u * pow(v, P - 2, P) % P)
