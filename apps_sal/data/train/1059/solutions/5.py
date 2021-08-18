N = eval(input())
A = []
for _ in range(N):
    A += [eval(input())]
B = []
for i in A:
    for j in A:
        B += [i % j]
print(max(B))
