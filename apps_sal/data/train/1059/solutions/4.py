N = eval(input())
A = []
for _ in range(N):
    A += [eval(input())]
B = [0]
A.sort()
for i in range(N):
    for j in range(i + 1, N):
        B += [A[i] % A[j]] + [A[j] % A[i]]
print(max(B))
