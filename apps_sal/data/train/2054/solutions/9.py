n = int(input())
u, v = [], []
for i in range(n - 1):
    a, b = list(map(int, input().split()))
    u.append(a)
    v.append(b)

colors = [0] + [int(x) for x in input().split()]

maximumDifference = 0
differences = {i: 0 for i in range(1, n + 1)}

for i in range(n - 1):
    vertex1 = u[i]
    vertex2 = v[i]

    if colors[vertex1] != colors[vertex2]:
        maximumDifference += 1
        differences[vertex1] += 1
        differences[vertex2] += 1

if maximumDifference in list(differences.values()):
    print('YES')
    print(list(differences.values()).index(maximumDifference) + 1)
else:
    print("NO")
